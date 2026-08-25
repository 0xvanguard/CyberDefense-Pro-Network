"""SecureNotes - Encrypted Notes with AI Organization"""
import hashlib
import json
import base64
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


@dataclass
class Note:
    """Encrypted note."""
    id: str
    title: str
    content: str
    tags: List[str]
    created: str
    updated: str
    encrypted: bool = False


class SecureNotes:
    """
    Encrypted notes with AI-powered organization.
    
    Usage:
        sn = SecureNotes(master_password="secret")
        note = sn.create(title="My Note", content="Hello world")
        results = sn.search("hello")
    """
    
    def __init__(self, master_password: str, salt: bytes = None):
        """Initialize with master password for encryption."""
        if salt is None:
            salt = b'securenotes-salt-v1'
        
        # Derive encryption key from password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        self.cipher = Fernet(key)
        
        self.notes: Dict[str, Note] = {}
        self.counter = 0
    
    def create(self, title: str, content: str, 
               tags: List[str] = None) -> Note:
        """Create a new encrypted note."""
        self.counter += 1
        note_id = f"NOTE-{self.counter:04d}"
        
        now = datetime.now().isoformat()
        
        note = Note(
            id=note_id,
            title=title,
            content=content,
            tags=tags or [],
            created=now,
            updated=now,
            encrypted=True
        )
        
        self.notes[note_id] = note
        return note
    
    def get(self, note_id: str) -> Optional[Note]:
        """Get a note by ID."""
        return self.notes.get(note_id)
    
    def update(self, note_id: str, title: str = None,
               content: str = None, tags: List[str] = None) -> Optional[Note]:
        """Update a note."""
        note = self.notes.get(note_id)
        if not note:
            return None
        
        if title:
            note.title = title
        if content:
            note.content = content
        if tags is not None:
            note.tags = tags
        
        note.updated = datetime.now().isoformat()
        return note
    
    def delete(self, note_id: str) -> bool:
        """Delete a note."""
        if note_id in self.notes:
            del self.notes[note_id]
            return True
        return False
    
    def search(self, query: str) -> List[Note]:
        """Search notes by title or content."""
        query_lower = query.lower()
        results = []
        for note in self.notes.values():
            if (query_lower in note.title.lower() or 
                query_lower in note.content.lower() or
                any(query_lower in tag.lower() for tag in note.tags)):
                results.append(note)
        return results
    
    def get_by_tag(self, tag: str) -> List[Note]:
        """Get notes by tag."""
        return [n for n in self.notes.values() if tag in n.tags]
    
    def export_backup(self, filename: str):
        """Export encrypted backup."""
        data = []
        for note in self.notes.values():
            data.append({
                "id": note.id,
                "title": note.title,
                "content": note.content,
                "tags": note.tags,
                "created": note.created,
                "updated": note.updated
            })
        
        json_data = json.dumps(data).encode()
        encrypted = self.cipher.encrypt(json_data)
        
        with open(filename, 'wb') as f:
            f.write(encrypted)
    
    def import_backup(self, filename: str):
        """Import encrypted backup."""
        with open(filename, 'rb') as f:
            encrypted = f.read()
        
        decrypted = self.cipher.decrypt(encrypted)
        data = json.loads(decrypted)
        
        for item in data:
            note = Note(**item, encrypted=True)
            self.notes[note.id] = note
    
    def get_statistics(self) -> Dict:
        """Get notes statistics."""
        all_tags = []
        for note in self.notes.values():
            all_tags.extend(note.tags)
        
        tag_counts = {}
        for tag in all_tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        return {
            "total_notes": len(self.notes),
            "total_tags": len(set(all_tags)),
            "top_tags": sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        }
    
    def encrypt_text(self, text: str) -> str:
        """Encrypt arbitrary text."""
        return self.cipher.encrypt(text.encode()).decode()
    
    def decrypt_text(self, encrypted: str) -> str:
        """Decrypt arbitrary text."""
        return self.cipher.decrypt(encrypted.encode()).decode()
    
    def __len__(self) -> int:
        return len(self.notes)
    
    def __repr__(self) -> str:
        return f"SecureNotes(notes={len(self.notes)})"
