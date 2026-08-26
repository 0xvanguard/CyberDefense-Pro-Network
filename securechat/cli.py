#!/usr/bin/env python3
"""
SecureChat CLI — Encrypted messaging from the command line.

Usage:
    python cli.py user --name Alice
    python cli.py send --to Bob --message "Hello!"
    python cli.py room --create "Secret Group"
    python cli.py room --join ROOM-0001
    python cli.py room --send ROOM-0001 --message "Hello group!"
    python cli.py rooms
    python cli.py messages
    python cli.py stats
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from chat import SecureChat, ChatRoom, MessageType


# Simple in-memory user store for demo
_users = {}


def get_user(name: str) -> SecureChat:
    if name not in _users:
        _users[name] = SecureChat(name=name)
    return _users[name]


def cmd_user(args):
    """Create/get a user."""
    user = get_user(args.name)
    print(f"\n👤 User: {user.name}")
    print(f"  Public Key: {user.get_public_key_hex()}")
    print(f"  Messages:   {len(user)}")


def cmd_send(args):
    """Send a direct message."""
    sender = get_user(args.from_name)
    recipient = get_user(args.to)

    encrypted = sender.send(recipient.get_public_key(), args.message)

    # Simulate receive
    decrypted = recipient.receive(sender.get_public_key(), encrypted)

    print(f"\n💬 Message Sent\n{'='*40}")
    print(f"  From:    {sender.name}")
    print(f"  To:      {args.to}")
    print(f"  Encrypted: {encrypted[:40]}...")
    print(f"  Decrypted: {decrypted}")
    print(f"  🔐 E2E Encrypted: ✅")


def cmd_room(args):
    """Manage rooms."""
    user = get_user(args.name)

    if args.create:
        room = user.create_room(args.create, description=args.description or "")
        print(f"\n🏠 Room Created\n{'='*40}")
        print(f"  ID:          {room.id}")
        print(f"  Name:        {room.name}")
        print(f"  Created by:  {room.created_by}")
        print(f"  Encrypted:   {'✅' if room.encrypted else '❌'}")

    elif args.join:
        ok = user.join_room(args.join)
        if ok:
            print(f"\n✅ Joined room: {args.join}")
        else:
            print(f"\n❌ Could not join room: {args.join}")

    elif args.leave:
        ok = user.leave_room(args.leave)
        if ok:
            print(f"\n✅ Left room: {args.leave}")
        else:
            print(f"\n❌ Could not leave room: {args.leave}")

    elif args.send_room:
        msg = user.send_room_message(args.send_room, args.message or "Hello!")
        if msg:
            print(f"\n💬 Room Message Sent\n{'='*40}")
            print(f"  Room:    {args.send_room}")
            print(f"  Sender:  {user.name}")
            print(f"  ID:      {msg.id}")
            print(f"  🔐 E2E Encrypted: ✅")
        else:
            print(f"\n❌ Not a member of room: {args.send_room}")

    elif args.info:
        members = user.get_room_members(args.info)
        print(f"\n🏠 Room: {args.info}")
        print(f"  Members: {', '.join(members)}")


def cmd_rooms(args):
    """List rooms."""
    user = get_user(args.name)
    rooms = user.get_rooms()

    print(f"\n🏠 Rooms ({len(rooms)})\n{'='*50}")
    for room in rooms:
        print(f"  {room.id} — {room.name} ({len(room.members)} members)")
        print(f"    Encrypted: {'✅' if room.encrypted else '❌'}")
        print(f"    Created: {room.created_by}")


def cmd_messages(args):
    """List messages."""
    user = get_user(args.name)

    if args.room:
        messages = user.get_room_messages(args.room)
        label = f"Room: {args.room}"
    else:
        messages = user.messages
        label = "all"

    print(f"\n💬 Messages ({label}) — {len(messages)}\n{'='*60}")
    for msg in messages[-20:]:
        type_icon = {"text": "💬", "image": "🖼️", "file": "📎", "system": "⚙️"}.get(msg.message_type, "💬")
        content = msg.content[:40] + "..." if len(msg.content) > 40 else msg.content
        print(f"  {type_icon} {msg.id} | {msg.sender} | {msg.timestamp[:19]}")
        print(f"     {content}")


def cmd_react(args):
    """Add/remove reaction."""
    user = get_user(args.name)

    if args.remove:
        ok = user.remove_reaction(args.message_id, args.reaction)
        action = "Removed" if ok else "Failed to remove"
    else:
        ok = user.add_reaction(args.message_id, args.reaction)
        action = "Added" if ok else "Failed to add"

    print(f"\n{action} reaction '{args.reaction}' on {args.message_id}")


def cmd_search(args):
    """Search messages."""
    user = get_user(args.name)
    results = user.search_messages(args.query)

    print(f"\n🔍 Search: '{args.query}' — {len(results)} results\n{'='*60}")
    for msg in results:
        print(f"  {msg.id} | {msg.sender} | {msg.timestamp[:19]}")


def cmd_stats(args):
    """Show statistics."""
    user = get_user(args.name)
    stats = user.get_statistics()

    print(f"\n📊 Chat Statistics\n{'='*40}")
    print(f"  User:           {stats['user']}")
    print(f"  Messages:       {stats['total_messages']}")
    print(f"  Rooms:          {stats['total_rooms']}")
    print(f"  Contacts:       {stats['total_contacts']}")
    print(f"  Unread:         {stats['unread']}")

    if stats["by_type"]:
        print(f"\n  By Type:")
        for msg_type, count in stats["by_type"].items():
            print(f"    {msg_type:<15} {count}")


def cmd_demo(args):
    """Run a demo conversation."""
    print("\n🎬 SecureChat Demo\n" + "="*50)

    alice = SecureChat(name="Alice")
    bob = SecureChat(name="Bob")

    print(f"\n👤 Alice created (key: {alice.get_public_key_hex()})")
    print(f"👤 Bob created (key: {bob.get_public_key_hex()})")

    # Alice sends to Bob
    encrypted = alice.send(bob.get_public_key(), "Hey Bob! This is encrypted 🔐")
    decrypted = bob.receive(alice.get_public_key(), encrypted)

    print(f"\n💬 Alice → Bob:")
    print(f"  Encrypted: {encrypted[:50]}...")
    print(f"  Decrypted: {decrypted}")

    # Bob replies
    encrypted2 = bob.send(alice.get_public_key(), "Hi Alice! Got your message 👋")
    decrypted2 = alice.receive(bob.get_public_key(), encrypted2)

    print(f"\n💬 Bob → Alice:")
    print(f"  Encrypted: {encrypted2[:50]}...")
    print(f"  Decrypted: {decrypted2}")

    # Group chat
    room = alice.create_room("Secret Group", members=["Bob"])
    print(f"\n🏠 Room created: {room.name} ({room.id})")

    msg1 = alice.send_room_message(room.id, "Hello everyone! 🎉")
    msg2 = bob.send_room_message(room.id, "Hey! This room is encrypted too!")

    print(f"\n💬 Room messages:")
    for msg in alice.get_room_messages(room.id):
        print(f"  {msg.sender}: {msg.content}")

    print(f"\n🔐 All messages are end-to-end encrypted!")


def main():
    parser = argparse.ArgumentParser(
        description="💬 SecureChat — E2E Encrypted Messaging"
    )
    sub = parser.add_subparsers(dest="command")

    # user
    user_p = sub.add_parser("user", help="Create/get user")
    user_p.add_argument("--name", "-n", required=True)

    # send
    send_p = sub.add_parser("send", help="Send message")
    send_p.add_argument("--from", dest="from_name", default="Alice")
    send_p.add_argument("--to", "-t", required=True)
    send_p.add_argument("--message", "-m", required=True)

    # room
    room_p = sub.add_parser("room", help="Manage rooms")
    room_p.add_argument("--name", default="Alice")
    room_p.add_argument("--create", default="")
    room_p.add_argument("--description", default="")
    room_p.add_argument("--join", default="")
    room_p.add_argument("--leave", default="")
    room_p.add_argument("--send-room", default="")
    room_p.add_argument("--info", default="")
    room_p.add_argument("--message", "-m", default="")

    # rooms
    rooms_p = sub.add_parser("rooms", help="List rooms")
    rooms_p.add_argument("--name", default="Alice")

    # messages
    msgs_p = sub.add_parser("messages", help="List messages")
    msgs_p.add_argument("--name", default="Alice")
    msgs_p.add_argument("--room", default="")

    # react
    react_p = sub.add_parser("react", help="Add/remove reaction")
    react_p.add_argument("--name", default="Alice")
    react_p.add_argument("message_id")
    react_p.add_argument("reaction")
    react_p.add_argument("--remove", action="store_true")

    # search
    search_p = sub.add_parser("search", help="Search messages")
    search_p.add_argument("--name", default="Alice")
    search_p.add_argument("query")

    # stats
    stats_p = sub.add_parser("stats", help="Statistics")
    stats_p.add_argument("--name", default="Alice")

    # demo
    sub.add_parser("demo", help="Run demo conversation")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "user": cmd_user, "send": cmd_send, "room": cmd_room,
        "rooms": cmd_rooms, "messages": cmd_messages, "react": cmd_react,
        "search": cmd_search, "stats": cmd_stats, "demo": cmd_demo,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
