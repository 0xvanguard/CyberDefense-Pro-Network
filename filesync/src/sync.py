"""FileSync — Encrypted File Synchronization"""
import hashlib
import os
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

class SyncStatus(Enum):
    SYNCED = "synced"
    PENDING = "pending"
    CONFLICT = "conflict"
    ERROR = "error"

@dataclass
class SyncResult:
    files_synced: int
    files_conflict: int
    files_error: int
    total_bytes: int

class FileSync:
    def __init__(self, sync_dir: str = "/sync"):
        self.sync_dir = sync_dir
        self.files: Dict[str, Dict] = {}
        self.sync_history: List[SyncResult] = []

    def add_file(self, name: str, content: bytes, encrypted: bool = False) -> Dict:
        file_hash = hashlib.sha256(content).hexdigest()
        self.files[name] = {"hash": file_hash, "size": len(content), "encrypted": encrypted, "status": "synced"}
        return self.files[name]

    def sync(self) -> SyncResult:
        synced = sum(1 for f in self.files.values() if f["status"] == "synced")
        conflict = sum(1 for f in self.files.values() if f["status"] == "conflict")
        total_bytes = sum(f["size"] for f in self.files.values())
        result = SyncResult(synced, conflict, 0, total_bytes)
        self.sync_history.append(result)
        return result

    def get_status(self, name: str) -> Optional[str]:
        f = self.files.get(name)
        return f["status"] if f else None

    def get_statistics(self) -> Dict:
        return {"total_files": len(self.files), "total_syncs": len(self.sync_history)}

    def __len__(self) -> int:
        return len(self.files)

    def __repr__(self) -> str:
        return f"FileSync(files={len(self.files)})"
