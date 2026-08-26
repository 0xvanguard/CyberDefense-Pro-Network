"""Tests for PasswordVault"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vault import PasswordVault, VaultEntry, PasswordStrength, StrengthAnalyzer, PasswordGenerator


vault = PasswordVault(master_password="test-password-123")
analyzer = StrengthAnalyzer()
generator = PasswordGenerator()


def test_vault_init():
    assert len(vault) == 0
    print("✅ Vault init OK")


def test_add_entry():
    entry = vault.add(service="github.com", username="user@email.com", password="mypass123")
    assert isinstance(entry, VaultEntry)
    assert entry.service == "github.com"
    assert entry.encrypted_password != "mypass123"
    print(f"✅ Add entry: {entry.id}")


def test_add_with_category():
    entry = vault.add(service="gmail.com", username="user@gmail.com", password="pass", category="email")
    assert entry.category == "email"
    print("✅ Add with category OK")


def test_add_favorite():
    entry = vault.add(service="aws.amazon.com", username="admin", password="pass", favorite=True)
    assert entry.favorite is True
    print("✅ Add favorite OK")


def test_get_by_service():
    entry = vault.get("github.com")
    assert entry is not None
    assert entry.service == "github.com"
    print("✅ Get by service OK")


def test_get_by_id():
    entry = vault.add(service="test.com", username="test", password="pass")
    got = vault.get_by_id(entry.id)
    assert got is not None
    print("✅ Get by ID OK")


def test_get_nonexistent():
    assert vault.get("nonexistent.com") is None
    print("✅ Get nonexistent OK")


def test_decrypt_password():
    entry = vault.add(service="decrypt-test.com", username="user", password="secret123")
    password = vault.get_password(entry.id)
    assert password == "secret123"
    print("✅ Decrypt password OK")


def test_update_entry():
    entry = vault.add(service="update-test.com", username="old", password="pass")
    updated = vault.update(entry.id, username="new", password="newpass")
    assert updated.username == "new"
    assert vault.get_password(entry.id) == "newpass"
    print("✅ Update entry OK")


def test_delete_entry():
    entry = vault.add(service="delete-test.com", username="user", password="pass")
    ok = vault.delete(entry.id)
    assert ok is True
    assert vault.get("delete-test.com") is None
    print("✅ Delete entry OK")


def test_delete_nonexistent():
    ok = vault.delete("ENTRY-9999")
    assert ok is False
    print("✅ Delete nonexistent OK")


def test_search():
    vault.add(service="search-github.com", username="user", password="pass")
    results = vault.search("search-github")
    assert len(results) > 0
    print("✅ Search OK")


def test_list_entries():
    vault.add(service="list-test.com", username="user", password="pass", category="work")
    entries = vault.list_entries(category="work")
    assert len(entries) > 0
    print("✅ List entries OK")


def test_list_favorites():
    vault.add(service="fav-test.com", username="user", password="pass", favorite=True)
    favs = vault.list_entries(favorite_only=True)
    assert len(favs) > 0
    print("✅ List favorites OK")


def test_toggle_favorite():
    entry = vault.add(service="toggle-test-2.com", username="user", password="pass")
    assert entry.favorite is False
    vault.toggle_favorite(entry.id)
    assert vault.get_by_id(entry.id).favorite is True
    vault.toggle_favorite(entry.id)
    assert vault.get_by_id(entry.id).favorite is False
    print("✅ Toggle favorite OK")


def test_strength_weak():
    strength = analyzer.analyze("123")
    assert strength.score < 20
    assert strength.label == "Very Weak"
    print(f"✅ Weak password: {strength.score}/100 ({strength.label})")


def test_strength_strong():
    strength = analyzer.analyze("MyStr0ng!P@ssw0rd#2024")
    assert strength.score >= 60
    assert strength.label in ("Strong", "Very Strong")
    print(f"✅ Strong password: {strength.score}/100 ({strength.label})")


def test_strength_common():
    strength = analyzer.analyze("password")
    assert strength.score <= 10
    print(f"✅ Common password: {strength.score}/100")


def test_strength_entropy():
    strength = analyzer.analyze("abcdefghij")
    assert strength.entropy > 0
    assert strength.charset_size == 26
    print(f"✅ Entropy: {strength.entropy} bits, charset: {strength.charset_size}")


def test_strength_features():
    strength = analyzer.analyze("Abc123!@#")
    assert strength.has_uppercase is True
    assert strength.has_lowercase is True
    assert strength.has_digits is True
    assert strength.has_symbols is True
    print("✅ Strength features OK")


def test_strength_crack_time():
    strength = analyzer.analyze("a")
    assert strength.crack_time != ""
    strength2 = analyzer.analyze("MyStr0ng!P@ssw0rd#2024xyz")
    print(f"✅ Crack time: {strength2.crack_time}")


def test_generate_password():
    pw = generator.generate(length=20)
    assert len(pw) == 20
    assert any(c.isupper() for c in pw)
    assert any(c.isdigit() for c in pw)
    print(f"✅ Generated: {pw}")


def test_generate_no_symbols():
    pw = generator.generate(length=16, symbols=False)
    assert len(pw) == 16
    assert not any(c in "!@#$%^&*" for c in pw)
    print(f"✅ No symbols: {pw}")


def test_generate_passphrase():
    pp = generator.generate_passphrase(words=4)
    assert pp.count("-") == 3
    assert len(pp) > 10
    print(f"✅ Passphrase: {pp}")


def test_vault_analyze():
    strength = vault.analyze_password("TestPassword123!")
    assert isinstance(strength, PasswordStrength)
    print(f"✅ Vault analyze: {strength.score}/100")


def test_vault_generate():
    pw = vault.generate_password(length=20)
    assert len(pw) == 20
    print(f"✅ Vault generate: {pw}")


def test_vault_passphrase():
    pp = vault.generate_passphrase(words=5)
    assert pp.count("-") == 4
    print(f"✅ Vault passphrase: {pp}")


def test_export_import():
    vault.add(service="export-test.com", username="user", password="pass")
    with tempfile.NamedTemporaryFile(suffix=".enc", delete=False) as f:
        path = f.name
    try:
        vault.export_vault(path)
        vault2 = PasswordVault(master_password="test-password-123")
        vault2.import_vault(path)
        assert len(vault2) > 0
    finally:
        os.unlink(path)
    print("✅ Export/import OK")


def test_statistics():
    stats = vault.get_statistics()
    assert "total_entries" in stats
    assert "categories" in stats
    assert "strength_distribution" in stats
    print(f"✅ Statistics: {stats['total_entries']} entries")


def test_entry_to_dict():
    entry = vault.add(service="dict-test.com", username="user", password="pass")
    d = entry.to_dict()
    assert d["service"] == "dict-test.com"
    assert "strength_score" in d
    print("✅ Entry to_dict OK")


def test_len():
    initial = len(vault)
    vault.add(service="len-test.com", username="user", password="pass")
    assert len(vault) == initial + 1
    print(f"✅ Len: {len(vault)} entries")


def test_strength_to_dict():
    strength = analyzer.analyze("TestPassword123!")
    d = strength.to_dict()
    assert "score" in d
    assert "label" in d
    assert "entropy" in d
    print("✅ Strength to_dict OK")


if __name__ == "__main__":
    test_vault_init()
    test_add_entry()
    test_add_with_category()
    test_add_favorite()
    test_get_by_service()
    test_get_by_id()
    test_get_nonexistent()
    test_decrypt_password()
    test_update_entry()
    test_delete_entry()
    test_delete_nonexistent()
    test_search()
    test_list_entries()
    test_list_favorites()
    test_toggle_favorite()
    test_strength_weak()
    test_strength_strong()
    test_strength_common()
    test_strength_entropy()
    test_strength_features()
    test_strength_crack_time()
    test_generate_password()
    test_generate_no_symbols()
    test_generate_passphrase()
    test_vault_analyze()
    test_vault_generate()
    test_vault_passphrase()
    test_export_import()
    test_statistics()
    test_entry_to_dict()
    test_len()
    test_strength_to_dict()
    print("\n🎉 All 32 tests passed!")
