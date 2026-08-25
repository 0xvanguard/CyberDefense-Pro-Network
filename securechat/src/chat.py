"""SecureChat - End-to-End Encrypted Messaging"""
import hashlib
import json
import base64
import os
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


@dataclass
class Message:
    """Encrypted message."""
    id: str
    sender: str
    recipient: str
    encrypted_content: str
    timestamp: str
    expired: bool = False
    read: bool = False


class SecureChat:
    """
    End-to-end encrypted messaging.
    
    Usage:
        alice = SecureChat(name="Alice")
        bob = SecureChat(name="Bob")
        
        encrypted = alice.send(bob.get_public_key(), "Hello!")
        decrypted = bob.receive(alice.get_public_key(), encrypted)
    """
    
    def __init__(self, name: str):
        """Initialize with user name and generate key pair."""
        self.name = name
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()
        
        self.messages: List[Message] = []
        self.contacts: Dict[str, bytes] = {}
        self.counter = 0
    
    def get_public_key(self) -> bytes:
        """Get public key in bytes."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    def get_public_key_hex(self) -> str:
        """Get public key as hex string."""
        return self.get_public_key().hex()[:64] + "..."
    
    def _derive_shared_key(self, other_public_key_bytes: bytes) -> bytes:
        """Derive shared secret from ECDH key exchange."""
        other_public_key = serialization.load_pem_public_key(other_public_key_bytes)
        
        shared_key = self.private_key.exchange(ec.ECDH(), other_public_key)
        
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'securechat-v1',
        ).derive(shared_key)
        
        return derived_key
    
    def send(self, recipient_key: bytes, content: str) -> str:
        """
        Send an encrypted message.
        
        Args:
            recipient_key: Recipient's public key
            content: Message content
            
        Returns:
            Encrypted message as base64 string
        """
        # Derive shared key
        shared_key = self._derive_shared_key(recipient_key)
        
        # Generate nonce
        nonce = os.urandom(12)
        
        # Encrypt with AES-256-GCM
        aesgcm = AESGCM(shared_key)
        encrypted = aesgcm.encrypt(nonce, content.encode(), None)
        
        # Combine nonce + encrypted
        combined = nonce + encrypted
        
        # Encode to base64
        encoded = base64.b64encode(combined).decode()
        
        # Create message
        self.counter += 1
        message = Message(
            id=f"MSG-{self.counter:06d}",
            sender=self.name,
            recipient="unknown",
            encrypted_content=encoded,
            timestamp=datetime.now().isoformat()
        )
        self.messages.append(message)
        
        return encoded
    
    def receive(self, sender_key: bytes, encrypted_content: str) -> str:
        """
        Receive and decrypt a message.
        
        Args:
            sender_key: Sender's public key
            encrypted_content: Encrypted message
            
        Returns:
            Decrypted message content
        """
        # Derive shared key
        shared_key = self._derive_shared_key(sender_key)
        
        # Decode from base64
        combined = base64.b64decode(encrypted_content)
        
        # Split nonce and encrypted data
        nonce = combined[:12]
        encrypted = combined[12:]
        
        # Decrypt with AES-256-GCM
        aesgcm = AESGCM(shared_key)
        decrypted = aesgcm.decrypt(nonce, encrypted, None)
        
        return decrypted.decode()
    
    def send_text(self, recipient_key: bytes, content: str, 
                  expire_seconds: int = None) -> Message:
        """Send a message with optional expiration."""
        encrypted = self.send(recipient_key, content)
        
        self.counter += 1
        message = Message(
            id=f"MSG-{self.counter:06d}",
            sender=self.name,
            recipient="unknown",
            encrypted_content=encrypted,
            timestamp=datetime.now().isoformat()
        )
        
        self.messages.append(message)
        return message
    
    def get_messages(self) -> List[Message]:
        """Get all messages."""
        return self.messages.copy()
    
    def get_conversation(self, contact: str) -> List[Message]:
        """Get messages with a specific contact."""
        return [m for m in self.messages 
                if m.sender == contact or m.recipient == contact]
    
    def delete_message(self, message_id: str) -> bool:
        """Delete a message."""
        for i, msg in enumerate(self.messages):
            if msg.id == message_id:
                del self.messages[i]
                return True
        return False
    
    def get_statistics(self) -> Dict:
        """Get chat statistics."""
        return {
            "total_messages": len(self.messages),
            "total_contacts": len(self.contacts),
            "user": self.name
        }
    
    def __len__(self) -> int:
        return len(self.messages)
    
    def __repr__(self) -> str:
        return f"SecureChat(name={self.name}, messages={len(self.messages)})"
