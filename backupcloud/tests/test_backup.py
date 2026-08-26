"""Tests for BackupCloud"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.backup import BackupCloud, BackupJob, BackupStatus

def test_status_enum():
    assert BackupStatus.COMPLETE.value == "complete"
    assert BackupStatus.FAILED.value == "failed"
    print("✅ BackupStatus enum OK")

def test_init():
    b = BackupCloud(provider="aws")
    assert b.provider == "aws"
    assert len(b) == 0
    print("✅ BackupCloud init OK")

def test_create_backup():
    b = BackupCloud()
    job = b.create_backup("Daily Backup", 100, 1024000)
    assert job.id.startswith("BK-")
    assert job.encrypted is True
    print(f"✅ Create backup: {job.id}")

def test_get_job():
    b = BackupCloud()
    job = b.create_backup("Test", 10, 1000)
    got = b.get_job(job.id)
    assert got is not None
    assert got.name == "Test"
    print("✅ Get job OK")

def test_get_job_nonexistent():
    b = BackupCloud()
    assert b.get_job("BK-9999") is None
    print("✅ Get nonexistent OK")

def test_unencrypted():
    b = BackupCloud()
    job = b.create_backup("Plain", 5, 500, encrypted=False)
    assert job.encrypted is False
    print("✅ Unencrypted backup OK")

def test_statistics():
    b = BackupCloud()
    b.create_backup("A", 10, 1000)
    b.create_backup("B", 20, 2000)
    stats = b.get_statistics()
    assert stats["total_jobs"] == 2
    assert stats["total_size"] == 3000
    print("✅ Statistics OK")

def test_multiple_backups():
    b = BackupCloud()
    for i in range(5):
        b.create_backup(f"Backup {i}", i * 10, i * 1000)
    assert len(b) == 5
    print("✅ Multiple backups OK")

if __name__ == "__main__":
    test_status_enum()
    test_init()
    test_create_backup()
    test_get_job()
    test_get_job_nonexistent()
    test_unencrypted()
    test_statistics()
    test_multiple_backups()
    print("\n🎉 All 8 tests passed!")
