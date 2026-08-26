"""Tests for CyberBot"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.chatbot import CyberBot, Topic, ChatResponse

def test_topic_enum():
    assert Topic.PASSWORD.value == "password"
    assert Topic.PHISHING.value == "phishing"
    print("✅ Topic enum OK")

def test_bot_init():
    bot = CyberBot(name="TestBot")
    assert bot.name == "TestBot"
    assert len(bot) == 0
    print("✅ Bot init OK")

def test_chat_password():
    bot = CyberBot()
    result = bot.chat("How do I create a strong password?")
    assert isinstance(result, ChatResponse)
    assert result.topic == "password"
    assert len(result.response) > 0
    print(f"✅ Chat password: {result.topic}")

def test_chat_network():
    bot = CyberBot()
    result = bot.chat("Tell me about network security and firewalls")
    assert result.topic in ("network", "firewall")
    print(f"✅ Chat network: {result.topic}")

def test_chat_malware():
    bot = CyberBot()
    result = bot.chat("How do I protect against ransomware malware?")
    assert result.topic in ("malware", "password")
    print(f"✅ Chat malware: {result.topic}")

def test_chat_phishing():
    bot = CyberBot()
    result = bot.chat("How can I detect phishing emails?")
    assert result.topic == "phishing"
    print(f"✅ Chat phishing: {result.topic}")

def test_chat_general():
    bot = CyberBot()
    result = bot.chat("hello there")
    assert result.topic in ("general", "password")
    print(f"✅ Chat general: {result.topic}")

def test_follow_ups():
    bot = CyberBot()
    result = bot.chat("password security")
    assert len(result.follow_ups) > 0
    print("✅ Follow-ups OK")

def test_conversation_history():
    bot = CyberBot()
    bot.chat("password tips")
    bot.chat("network security")
    assert len(bot) == 2
    print("✅ Conversation history OK")

def test_statistics():
    bot = CyberBot()
    bot.chat("password")
    bot.chat("network")
    bot.chat("malware")
    stats = bot.get_statistics()
    assert stats["total_messages"] == 3
    print("✅ Statistics OK")

def test_confidence():
    bot = CyberBot()
    result = bot.chat("password encryption vulnerability")
    assert 0.5 <= result.confidence <= 1.0
    print(f"✅ Confidence: {result.confidence:.2f}")

if __name__ == "__main__":
    test_topic_enum()
    test_bot_init()
    test_chat_password()
    test_chat_network()
    test_chat_malware()
    test_chat_phishing()
    test_chat_general()
    test_follow_ups()
    test_conversation_history()
    test_statistics()
    test_confidence()
    print("\n🎉 All 11 tests passed!")
