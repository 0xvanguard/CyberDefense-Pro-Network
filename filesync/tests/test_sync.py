"""Tests for FileSync"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.sync import FileSync, SyncStatus, SyncResult

def test_sync_status():
    assert SyncStatus.SYNCED.value == "synced"
    assert SyncStatus.CONFLICT.value == "conflict"
    print("✅ SyncStatus enum OK")

def test_sync_init():
    fs = FileSync()
    assert len(fs) == 0
    print("✅ FileSync init OK")

def test_add_file():
    fs = FileSync()
    info = fs.add_file("test.txt", b"hello world")
    assert info["hash"] != ""
    assert info["size"] == 11
    print("✅ Add file OK")

def test_add_encrypted():
    fs = FileSync()
    info = fs.add_file("secret.txt", b"encrypted", encrypted=True)
    assert info["encrypted"] is True
    print("✅ Add encrypted OK")

def test_sync():
    fs = FileSync()
    fs.add_file("a.txt", b"content a")
    fs.add_file("b.txt", b"content b")
    result = fs.sync()
    assert result.files_synced == 2
    assert result.total_bytes > 0
    print(f"✅ Sync: {result.files_synced} files, {result.total_bytes} bytes")

def test_get_status():
    fs = FileSync()
    fs.add_file("test.txt", b"data")
    assert fs.get_status("test.txt") == "synced"
    assert fs.get_status("missing.txt") is None
    print("✅ Get status OK")

def test_statistics():
    fs = FileSync()
    fs.add_file("a.txt", b"data")
    fs.sync()
    stats = fs.get_statistics()
    assert stats["total_files"] == 1
    assert stats["total_syncs"] == 1
    print("✅ Statistics OK")

def test_multiple_syncs():
    fs = FileSync()
    fs.add_file("a.txt", b"data")
    fs.sync()
    fs.sync()
    assert len(fs.sync_history) == 2
    print("✅ Multiple syncs OK")

def test_file_hash_unique():
    fs = FileSync()
    f1 = fs.add_file("a.txt", b"content1")
    f2 = fs.add_file("b.txt", b"content2")
    assert f1["hash"] != f2["hash"]
    print("✅ Unique hashes OK")

if __name__ == "__main__":
    test_sync_status()
    test_sync_init()
    test_add_file()
    test_add_encrypted()
    test_sync()
    test_get_status()
    test_statistics()
    test_multiple_syncs()
    test_file_hash_unique()
    print("\n🎉 All 9 tests passed!")
