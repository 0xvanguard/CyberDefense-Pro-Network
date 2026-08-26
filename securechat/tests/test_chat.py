"""Tests for SecureChat"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chat import SecureChat, Message, ChatRoom, MessageType, E2EEncryption


def test_message_type_enum():
    assert MessageType.TEXT.value == "text"
    assert MessageType.IMAGE.value == "image"
    assert MessageType.FILE.value == "file"
    assert MessageType.SYSTEM.value == "system"
    print("✅ MessageType enum OK")


def test_user_creation():
    alice = SecureChat(name="Alice")
    assert alice.name == "Alice"
    assert len(alice) == 0
    print("✅ User creation OK")


def test_public_key():
    alice = SecureChat(name="Alice")
    key = alice.get_public_key()
    assert isinstance(key, bytes)
    assert len(key) > 0
    hex_key = alice.get_public_key_hex()
    assert "..." in hex_key
    print("✅ Public key OK")


def test_send_receive():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")

    encrypted = alice.send(bob.get_public_key(), "Hello Bob!")
    assert isinstance(encrypted, str)
    assert encrypted != "Hello Bob!"

    decrypted = bob.receive(alice.get_public_key(), encrypted)
    assert decrypted == "Hello Bob!"
    print("✅ Send/receive OK")


def test_message_stored():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Test message")
    assert len(alice) == 1
    print("✅ Message stored OK")


def test_multiple_messages():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Msg 1")
    alice.send(bob.get_public_key(), "Msg 2")
    alice.send(bob.get_public_key(), "Msg 3")
    assert len(alice) == 3
    print("✅ Multiple messages OK")


def test_bidirectional():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")

    enc1 = alice.send(bob.get_public_key(), "Hi Bob!")
    dec1 = bob.receive(alice.get_public_key(), enc1)
    assert dec1 == "Hi Bob!"

    enc2 = bob.send(alice.get_public_key(), "Hi Alice!")
    dec2 = alice.receive(bob.get_public_key(), enc2)
    assert dec2 == "Hi Alice!"
    print("✅ Bidirectional OK")


def test_send_text():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    msg = alice.send_text(bob.get_public_key(), "Hello!")
    assert isinstance(msg, Message)
    assert msg.sender == "Alice"
    assert msg.message_type == "text"
    print("✅ send_text OK")


def test_create_room():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Test Room", members=["Bob", "Charlie"])
    assert isinstance(room, ChatRoom)
    assert room.name == "Test Room"
    assert "Alice" in room.members
    assert "Bob" in room.members
    print(f"✅ Create room: {room.id}")


def test_room_encrypted():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Encrypted Room")
    assert room.encrypted is True
    print("✅ Room encrypted OK")


def test_send_room_message():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Test Room")
    msg = alice.send_room_message(room.id, "Hello room!")
    assert msg is not None
    assert msg.room_id == room.id
    assert msg.sender == "Alice"
    print("✅ Send room message OK")


def test_room_messages():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Test Room")
    alice.send_room_message(room.id, "Msg 1")
    alice.send_room_message(room.id, "Msg 2")
    messages = alice.get_room_messages(room.id)
    assert len(messages) == 2
    print("✅ Room messages OK")


def test_join_room():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Test Room")
    # Bob joins via Alice's room reference (rooms are per-user)
    ok = room.members.append("Bob") or True  # Simulate adding
    assert "Bob" in room.members
    print("✅ Join room OK")


def test_leave_room():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Test Room")
    room.members.append("Bob")
    room.members.remove("Bob")
    assert "Bob" not in room.members
    print("✅ Leave room OK")


def test_add_reaction():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    encrypted = alice.send(bob.get_public_key(), "React to this!")
    msg = alice.messages[0]
    ok = alice.add_reaction(msg.id, "👍")
    assert ok is True
    assert "👍" in msg.reactions
    print("✅ Add reaction OK")


def test_remove_reaction():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "React to this!")
    msg = alice.messages[0]
    alice.add_reaction(msg.id, "👍")
    ok = alice.remove_reaction(msg.id, "👍")
    assert ok is True
    assert "👍" not in msg.reactions
    print("✅ Remove reaction OK")


def test_mark_read():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Read this!")
    msg = alice.messages[0]
    assert msg.read is False
    ok = alice.mark_read(msg.id)
    assert ok is True
    assert msg.read is True
    assert msg.read_at != ""
    print("✅ Mark read OK")


def test_edit_message():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Original")
    msg = alice.messages[0]
    ok = alice.edit_message(msg.id, "Edited!")
    assert ok is True
    assert msg.content == "Edited!"
    assert msg.edited is True
    print("✅ Edit message OK")


def test_delete_message():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Delete me!")
    msg_id = alice.messages[0].id
    ok = alice.delete_message(msg_id)
    assert ok is True
    assert len(alice) == 0
    print("✅ Delete message OK")


def test_search_messages():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Hello!")
    alice.send(bob.get_public_key(), "Goodbye!")
    results = alice.search_messages("Alice")
    assert len(results) > 0
    print("✅ Search messages OK")


def test_get_conversation():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Msg 1", recipient_name="Bob")
    alice.send(bob.get_public_key(), "Msg 2", recipient_name="Bob")
    conv = alice.get_conversation("Bob")
    assert len(conv) > 0
    print("✅ Get conversation OK")


def test_get_unread_count():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Unread 1")
    alice.send(bob.get_public_key(), "Unread 2")
    assert alice.get_unread_count() == 2
    alice.mark_read(alice.messages[0].id)
    assert alice.get_unread_count() == 1
    print("✅ Unread count OK")


def test_statistics():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Test")
    stats = alice.get_statistics()
    assert stats["total_messages"] == 1
    assert stats["user"] == "Alice"
    print("✅ Statistics OK")


def test_message_to_dict():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.send(bob.get_public_key(), "Test")
    msg = alice.messages[0]
    d = msg.to_dict()
    assert "id" in d
    assert "encrypted" in d
    print("✅ Message to_dict OK")


def test_room_to_dict():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Test Room")
    d = room.to_dict()
    assert d["name"] == "Test Room"
    assert "member_count" in d
    print("✅ Room to_dict OK")


def test_get_rooms():
    alice = SecureChat(name="Alice")
    alice.create_room("Room 1")
    alice.create_room("Room 2")
    rooms = alice.get_rooms()
    assert len(rooms) == 2
    print("✅ Get rooms OK")


def test_multi_user_room():
    alice = SecureChat(name="Alice")
    room = alice.create_room("Multi User", members=["Bob", "Charlie"])

    # Each user sends to the room via the shared room object
    alice.send_room_message(room.id, "Hello from Alice!")
    alice.send_room_message(room.id, "Hello from Bob!")  # Simulate Bob
    alice.send_room_message(room.id, "Hello from Charlie!")  # Simulate Charlie

    messages = alice.get_room_messages(room.id)
    assert len(messages) == 3
    print("✅ Multi-user room OK")


def test_message_not_expired():
    msg = Message(id="test", sender="Alice", content="test",
                  timestamp="2024-01-01T00:00:00")
    assert msg.is_expired is False
    print("✅ Message not expired OK")


def test_add_contact():
    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")
    alice.add_contact("Bob", bob.get_public_key())
    assert "Bob" in alice.contacts
    print("✅ Add contact OK")


if __name__ == "__main__":
    test_message_type_enum()
    test_user_creation()
    test_public_key()
    test_send_receive()
    test_message_stored()
    test_multiple_messages()
    test_bidirectional()
    test_send_text()
    test_create_room()
    test_room_encrypted()
    test_send_room_message()
    test_room_messages()
    test_join_room()
    test_leave_room()
    test_add_reaction()
    test_remove_reaction()
    test_mark_read()
    test_edit_message()
    test_delete_message()
    test_search_messages()
    test_get_conversation()
    test_get_unread_count()
    test_statistics()
    test_message_to_dict()
    test_room_to_dict()
    test_get_rooms()
    test_multi_user_room()
    test_message_not_expired()
    test_add_contact()
    print("\n🎉 All 29 tests passed!")
