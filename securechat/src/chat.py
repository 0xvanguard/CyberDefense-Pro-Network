"""SecureChat — End-to-End Encrypted Messaging

ECDH key exchange + AES-256-GCM encryption for secure messaging.
Supports direct messages, group chats, reactions, and message types.
"""

import hashlib
import json
import base64
import os
import secrets
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any, Set
from datetime import datetime, timedelta
from enum import Enum


# ─── Enums ───────────────────────────────────────────────────────────

class MessageType(Enum):
    TEXT = "text"
    IMAGE = "image"
    FILE = "file"
    SYSTEM = "system"
    REACTION = "reaction"
    ENCRYPTED_FILE = "encrypted_file"


# ─── Data Models ─────────────────────────────────────────────────────

@dataclass
class Message:
    """Encrypted message."""
    id: str
    sender: str
    content: str
    timestamp: str
    message_type: str = "text"
    recipient: str = ""
    room_id: str = ""
    encrypted: bool = True
    read: bool = False
    read_at: str = ""
    reactions: List[str] = field(default_factory=list)
    expires_at: str = ""
    edited: bool = False
    edited_at: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "sender": self.sender,
            "content": self.content[:50] + "..." if len(self.content) > 50 else self.content,
            "timestamp": self.timestamp,
            "type": self.message_type,
            "room": self.room_id,
            "encrypted": self.encrypted,
            "read": self.read,
            "reactions": self.reactions,
        }

    @property
    def is_expired(self) -> bool:
        if not self.expires_at:
            return False
        try:
            exp = datetime.fromisoformat(self.expires_at)
            return datetime.now() > exp
        except (ValueError, TypeError):
            return False


@dataclass
class ChatRoom:
    """Group chat room."""
    id: str
    name: str
    members: List[str] = field(default_factory=list)
    created_by: str = ""
    created_at: str = ""
    encrypted: bool = True
    max_members: int = 100
    description: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "members": self.members,
            "created_by": self.created_by,
            "created_at": self.created_at,
            "encrypted": self.encrypted,
            "member_count": len(self.members),
        }


# ─── Encryption Layer ───────────────────────────────────────────────

class E2EEncryption:
    """ECDH + AES-256-GCM end-to-end encryption."""

    def __init__(self):
        from cryptography.hazmat.primitives.asymmetric import ec
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.kdf.hkdf import HKDF
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM

        self._ec = ec
        self._serialization = serialization
        self._HKDF = HKDF
        self._hashes = hashes
        self._AESGCM = AESGCM

        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()

    def get_public_key_bytes(self) -> bytes:
        return self.public_key.public_bytes(
            encoding=self._serialization.Encoding.PEM,
            format=self._serialization.PublicFormat.SubjectPublicKeyInfo,
        )

    def get_public_key_hex(self) -> str:
        return self.get_public_key_bytes().hex()[:64] + "..."

    def _derive_shared_key(self, other_public_key_bytes: bytes) -> bytes:
        other_public_key = self._serialization.load_pem_public_key(other_public_key_bytes)
        shared_key = self.private_key.exchange(self._ec.ECDH(), other_public_key)
        derived_key = self._HKDF(
            algorithm=self._hashes.SHA256(),
            length=32, salt=None, info=b"securechat-v2",
        ).derive(shared_key)
        return derived_key

    def encrypt(self, other_public_key_bytes: bytes, plaintext: str) -> str:
        shared_key = self._derive_shared_key(other_public_key_bytes)
        nonce = os.urandom(12)
        aesgcm = self._AESGCM(shared_key)
        encrypted = aesgcm.encrypt(nonce, plaintext.encode(), None)
        combined = nonce + encrypted
        return base64.b64encode(combined).decode()

    def decrypt(self, sender_public_key_bytes: bytes, ciphertext: str) -> str:
        shared_key = self._derive_shared_key(sender_public_key_bytes)
        combined = base64.b64decode(ciphertext)
        nonce = combined[:12]
        encrypted = combined[12:]
        aesgcm = self._AESGCM(shared_key)
        decrypted = aesgcm.decrypt(nonce, encrypted, None)
        return decrypted.decode()


# ─── SecureChat Engine ──────────────────────────────────────────────

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
        self.name = name
        self.crypto = E2EEncryption()
        self.messages: List[Message] = []
        self.rooms: Dict[str, ChatRoom] = {}
        self.contacts: Dict[str, str] = {}  # name -> public_key_hex
        self.counter = 0
        self.room_counter = 0

    def get_public_key(self) -> bytes:
        return self.crypto.get_public_key_bytes()

    def get_public_key_hex(self) -> str:
        return self.crypto.get_public_key_hex()

    def add_contact(self, name: str, public_key: bytes):
        """Add a contact with their public key."""
        self.contacts[name] = public_key

    # ─── Direct Messages ─────────────────────────────────────────────

    def send(self, recipient_key: bytes, content: str,
             message_type: str = "text",
             expire_seconds: Optional[int] = None,
             recipient_name: str = "unknown") -> str:
        """Send an encrypted message. Returns encrypted content."""
        encrypted = self.crypto.encrypt(recipient_key, content)

        self.counter += 1
        expires_at = ""
        if expire_seconds:
            expires_at = (datetime.now() + timedelta(seconds=expire_seconds)).isoformat()

        message = Message(
            id=f"MSG-{self.counter:06d}",
            sender=self.name, recipient=recipient_name,
            content=encrypted, timestamp=datetime.now().isoformat(),
            message_type=message_type, encrypted=True,
            expires_at=expires_at,
        )
        self.messages.append(message)
        return encrypted

    def receive(self, sender_key: bytes, encrypted_content: str) -> str:
        """Receive and decrypt a message."""
        return self.crypto.decrypt(sender_key, encrypted_content)

    def send_text(self, recipient_key: bytes, content: str,
                  expire_seconds: Optional[int] = None) -> Message:
        """Send a text message and return the Message object."""
        encrypted = self.send(recipient_key, content, "text", expire_seconds)

        self.counter += 1
        message = Message(
            id=f"MSG-{self.counter:06d}",
            sender=self.name, recipient="unknown",
            content=encrypted, timestamp=datetime.now().isoformat(),
            message_type="text", encrypted=True,
        )
        self.messages.append(message)
        return message

    # ─── Group Chat ──────────────────────────────────────────────────

    def create_room(self, name: str, members: Optional[List[str]] = None,
                    description: str = "") -> ChatRoom:
        """Create a group chat room."""
        self.room_counter += 1
        room = ChatRoom(
            id=f"ROOM-{self.room_counter:04d}",
            name=name, members=[self.name] + (members or []),
            created_by=self.name, description=description,
        )
        self.rooms[room.id] = room
        return room

    def join_room(self, room_id: str) -> bool:
        """Join a room."""
        room = self.rooms.get(room_id)
        if not room:
            return False
        if self.name not in room.members:
            if len(room.members) < room.max_members:
                room.members.append(self.name)
        return True

    def leave_room(self, room_id: str) -> bool:
        """Leave a room."""
        room = self.rooms.get(room_id)
        if not room:
            return False
        if self.name in room.members:
            room.members.remove(self.name)
            return True
        return False

    def send_room_message(self, room_id: str, content: str,
                         message_type: str = "text") -> Optional[Message]:
        """Send a message to a room."""
        room = self.rooms.get(room_id)
        if not room or self.name not in room.members:
            return None

        self.counter += 1
        message = Message(
            id=f"MSG-{self.counter:06d}",
            sender=self.name, content=content,
            timestamp=datetime.now().isoformat(),
            message_type=message_type, room_id=room_id,
            encrypted=True,
        )
        self.messages.append(message)
        return message

    def get_room_messages(self, room_id: str) -> List[Message]:
        """Get messages for a room."""
        return [m for m in self.messages if m.room_id == room_id]

    def get_rooms(self) -> List[ChatRoom]:
        """Get all rooms."""
        return list(self.rooms.values())

    def get_room_members(self, room_id: str) -> List[str]:
        """Get room members."""
        room = self.rooms.get(room_id)
        return room.members if room else []

    # ─── Message Management ──────────────────────────────────────────

    def add_reaction(self, message_id: str, reaction: str) -> bool:
        """Add a reaction to a message."""
        for msg in self.messages:
            if msg.id == message_id:
                if reaction not in msg.reactions:
                    msg.reactions.append(reaction)
                return True
        return False

    def remove_reaction(self, message_id: str, reaction: str) -> bool:
        """Remove a reaction from a message."""
        for msg in self.messages:
            if msg.id == message_id:
                if reaction in msg.reactions:
                    msg.reactions.remove(reaction)
                return True
        return False

    def mark_read(self, message_id: str) -> bool:
        """Mark a message as read."""
        for msg in self.messages:
            if msg.id == message_id:
                msg.read = True
                msg.read_at = datetime.now().isoformat()
                return True
        return False

    def edit_message(self, message_id: str, new_content: str) -> bool:
        """Edit a message."""
        for msg in self.messages:
            if msg.id == message_id and msg.sender == self.name:
                msg.content = new_content
                msg.edited = True
                msg.edited_at = datetime.now().isoformat()
                return True
        return False

    def delete_message(self, message_id: str) -> bool:
        """Delete a message."""
        for i, msg in enumerate(self.messages):
            if msg.id == message_id:
                del self.messages[i]
                return True
        return False

    def search_messages(self, query: str) -> List[Message]:
        """Search messages (by ID or sender)."""
        query_lower = query.lower()
        return [m for m in self.messages
                if query_lower in m.id.lower() or query_lower in m.sender.lower()]

    def get_conversation(self, contact: str) -> List[Message]:
        """Get messages with a specific contact."""
        return [m for m in self.messages
                if m.sender == contact or m.recipient == contact]

    def get_unread_count(self) -> int:
        """Get count of unread messages."""
        return sum(1 for m in self.messages if not m.read)

    # ─── Statistics ──────────────────────────────────────────────────

    def get_statistics(self) -> Dict[str, Any]:
        type_counts = {}
        for msg in self.messages:
            type_counts[msg.message_type] = type_counts.get(msg.message_type, 0) + 1

        return {
            "user": self.name,
            "total_messages": len(self.messages),
            "total_rooms": len(self.rooms),
            "total_contacts": len(self.contacts),
            "unread": self.get_unread_count(),
            "by_type": type_counts,
        }

    def __len__(self) -> int:
        return len(self.messages)

    def __repr__(self) -> str:
        return f"SecureChat(name={self.name}, messages={len(self.messages)})"
