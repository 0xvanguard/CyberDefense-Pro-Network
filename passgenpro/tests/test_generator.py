"""Tests for PassGen Pro."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from generator import PassGen, Password, EntropyAnalysis


def test_random_password():
    """Test random password generation."""
    gen = PassGen()
    password = gen.random(length=20)
    assert len(password.password) == 20
    assert password.entropy > 0
    assert password.strength in ["very_weak", "weak", "fair", "strong", "very_strong"]


def test_random_custom_length():
    """Test custom length."""
    gen = PassGen()
    for length in [8, 12, 16, 24, 32]:
        password = gen.random(length=length)
        assert len(password.password) == length


def test_random_no_symbols():
    """Test without symbols."""
    gen = PassGen()
    password = gen.random(length=20, symbols=False)
    assert not any(c in "!@#$%^&*()" for c in password.password)


def test_random_no_digits():
    """Test without digits."""
    gen = PassGen()
    password = gen.random(length=20, digits=False)
    assert not any(c.isdigit() for c in password.password)


def test_passphrase():
    """Test passphrase generation."""
    gen = PassGen()
    password = gen.passphrase(words=6)
    assert len(password.password.split("-")) == 7  # 6 words + 1 number
    assert password.entropy > 0


def test_passphrase_custom_separator():
    """Test custom separator."""
    gen = PassGen()
    password = gen.passphrase(words=4, separator=" ")
    assert " " in password.password


def test_pin():
    """Test PIN generation."""
    gen = PassGen()
    password = gen.pin(length=6)
    assert len(password.password) == 6
    assert password.password.isdigit()


def test_check_strength():
    """Test strength checking."""
    gen = PassGen()
    weak = gen.check_strength("abc")
    strong = gen.check_strength("MyStr0ng!P@ssw0rd#2024")
    assert strong.strength_score > weak.strength_score


def test_entropy_analysis():
    """Test entropy analysis."""
    gen = PassGen()
    password = gen.random(length=16)
    assert password.entropy_analysis.total_bits > 0
    assert password.entropy_analysis.charset_size > 0
    assert password.entropy_analysis.crack_time_display


def test_strength_bar():
    """Test strength bar generation."""
    gen = PassGen()
    password = gen.random(length=16)
    assert "█" in password.strength_bar
    assert "░" in password.strength_bar


def test_batch_generation():
    """Test batch generation."""
    gen = PassGen()
    passwords = gen.random_batch(count=5, length=12)
    assert len(passwords) == 5
    for p in passwords:
        assert len(p.password) == 12


def test_to_dict():
    """Test to_dict conversion."""
    gen = PassGen()
    password = gen.random()
    d = password.to_dict()
    assert isinstance(d, dict)
    assert "password" in d
    assert "entropy" in d
    assert "strength" in d


def test_to_json():
    """Test to_json conversion."""
    import json
    gen = PassGen()
    password = gen.random()
    j = password.to_json()
    data = json.loads(j)
    assert "password" in data


def test_exclude_ambiguous():
    """Test excluding ambiguous characters."""
    gen = PassGen()
    password = gen.random(length=50, exclude_ambiguous=True)
    assert not any(c in "0OolI1" for c in password.password)


def test_crack_time():
    """Test crack time formatting."""
    gen = PassGen()
    password = gen.random(length=20)
    assert password.crack_time
    assert "year" in password.crack_time.lower() or "million" in password.crack_time.lower() or "billion" in password.crack_time.lower()


if __name__ == "__main__":
    test_random_password()
    test_random_custom_length()
    test_random_no_symbols()
    test_random_no_digits()
    test_passphrase()
    test_passphrase_custom_separator()
    test_pin()
    test_check_strength()
    test_entropy_analysis()
    test_strength_bar()
    test_batch_generation()
    test_to_dict()
    test_to_json()
    test_exclude_ambiguous()
    test_crack_time()
    print("✅ All tests passed!")
