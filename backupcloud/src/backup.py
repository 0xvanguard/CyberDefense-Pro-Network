"""BackupCloud — Encrypted Cloud Backup"""
import hashlib
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum

class BackupStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"

@dataclass
class BackupJob:
    id: str
    name: str
    files_count: int
    total_size: int
    status: str
    encrypted: bool
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

class BackupCloud:
    def __init__(self, provider: str = "cloud"):
        self.provider = provider
        self.jobs: List[BackupJob] = []
        self.counter = 0

    def create_backup(self, name: str, files_count: int, total_size: int, encrypted: bool = True) -> BackupJob:
        self.counter += 1
        job = BackupJob(id=f"BK-{self.counter:04d}", name=name, files_count=files_count,
                       total_size=total_size, status="complete", encrypted=encrypted)
        self.jobs.append(job)
        return job

    def get_job(self, job_id: str) -> Optional[BackupJob]:
        for j in self.jobs:
            if j.id == job_id:
                return j
        return None

    def get_statistics(self) -> Dict:
        total_size = sum(j.total_size for j in self.jobs)
        return {"total_jobs": len(self.jobs), "total_size": total_size, "encrypted": sum(1 for j in self.jobs if j.encrypted)}

    def __len__(self) -> int:
        return len(self.jobs)

    def __repr__(self) -> str:
        return f"BackupCloud(jobs={len(self.jobs)})"
