"""PasswordVault - Modern Password Manager with Zero-Knowledge"""
import secrets
import string
import json
import base64
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


@dataclass
class VaultEntry:
    """Password vault entry."""
    id: str
    service: str
    username: str
    encrypted_password: str
    url: str = ""
    notes: str = ""
    category: str = "general"
    created: str = ""
    updated: str = ""
    favorite: bool = False


class PasswordVault:
    """
    Modern password manager with zero-knowledge architecture.
    
    Usage:
        vault = PasswordVault(master_password="secret")
        vault.add(service="github.com", username="user@email.com", password="pass123")
        entry = vault.get("github.com")
    """
    
    def __init__(self, master_password: str, salt: bytes = None):
        """Initialize vault with master password."""
        if salt is None:
            salt = b'passwordvault-salt-v1'
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        self.cipher = Fernet(key)
        
        self.entries: Dict[str, VaultEntry] = {}
        self.counter = 0
    
    def add(self, service: str, username: str, password: str,
            url: str = "", notes: str = "", 
            category: str = "general") -> VaultEntry:
        """Add a new password entry."""
        self.counter += 1
        entry_id = f"ENTRY-{self.counter:04d}"
        
        encrypted_pw = self.cipher.encrypt(password.encode()).decode()
        now = datetime.now().isoformat()
        
        entry = VaultEntry(
            id=entry_id,
            service=service,
            username=username,
            encrypted_password=encrypted_pw,
            url=url,
            notes=notes,
            category=category,
            created=now,
            updated=now
        )
        
        self.entries[entry_id] = entry
        return entry
    
    def get(self, service: str) -> Optional[VaultEntry]:
        """Get entry by service name."""
        for entry in self.entries.values():
            if entry.service.lower() == service.lower():
                return entry
        return None
    
    def get_by_id(self, entry_id: str) -> Optional[VaultEntry]:
        """Get entry by ID."""
        return self.entries.get(entry_id)
    
    def decrypt(self, encrypted_password: str) -> str:
        """Decrypt a password."""
        return self.cipher.decrypt(encrypted_password.encode()).decode()
    
    def update(self, entry_id: str, **kwargs) -> Optional[VaultEntry]:
        """Update an entry."""
        entry = self.entries.get(entry_id)
        if not entry:
            return None
        
        for key, value in kwargs.items():
            if key == "password":
                entry.encrypted_password = self.cipher.encrypt(value.encode()).decode()
            elif hasattr(entry, key):
                setattr(entry, key, value)
        
        entry.updated = datetime.now().isoformat()
        return entry
    
    def delete(self, entry_id: str) -> bool:
        """Delete an entry."""
        if entry_id in self.entries:
            del self.entries[entry_id]
            return True
        return False
    
    def search(self, query: str) -> List[VaultEntry]:
        """Search entries by service, username, or notes."""
        query_lower = query.lower()
        results = []
        for entry in self.entries.values():
            if (query_lower in entry.service.lower() or
                query_lower in entry.username.lower() or
                query_lower in entry.notes.lower()):
                results.append(entry)
        return results
    
    def get_by_category(self, category: str) -> List[VaultEntry]:
        """Get entries by category."""
        return [e for e in self.entries.values() if e.category == category]
    
    def generate_password(self, length: int = 16, 
                         uppercase: bool = True,
                         digits: bool = True,
                         symbols: bool = True) -> str:
        """Generate a secure password."""
        charset = string.ascii_lowercase
        if uppercase:
            charset += string.ascii_uppercase
        if digits:
            charset += string.digits
        if symbols:
            charset += "!@#$%^&*"
        
        return ''.join(secrets.choice(charset) for _ in range(length))
    
    def toggle_favorite(self, entry_id: str) -> bool:
        """Toggle favorite status."""
        entry = self.entries.get(entry_id)
        if entry:
            entry.favorite = not entry.favorite
            return True
        return False
    
    def get_favorites(self) -> List[VaultEntry]:
        """Get all favorite entries."""
        return [e for e in self.entries.values() if e.favorite]
    
    def export_vault(self, filename: str):
        """Export encrypted vault."""
        data = []
        for entry in self.entries.values():
            data.append({
                "id": entry.id,
                "service": entry.service,
                "username": entry.username,
                "encrypted_password": entry.encrypted_password,
                "url": entry.url,
                "notes": entry.notes,
                "category": entry.category,
                "created": entry.created,
                "updated": entry.updated,
                "favorite": entry.favorite
            })
        
        json_data = json.dumps(data).encode()
        encrypted = self.cipher.encrypt(json_data)
        
        with open(filename, 'wb') as f:
            f.write(encrypted)
    
    def get_statistics(self) -> Dict:
        """Get vault statistics."""
        categories = {}
        for entry in self.entries.values():
            categories[entry.category] = categories.get(entry.category, 0) + 1
        
        return {
            "total_entries": len(self.entries),
            "favorites": len(self.get_favorites()),
            "categories": categories
        }
    
    def __len__(self) -> int:
        return len(self.entries)
    
    def __repr__(self) -> str:
        return f"PasswordVault(entries={len(self.entries)})"
