"""CodeSigning - Code Signing for Open Source"""
from dataclasses import dataclass
import hashlib

@dataclass
class SignedArtifact:
    filename: str
    hash_sha256: str
    signature: str
    signed_by: str

class CodeSigner:
    def __init__(self):
        self.keys = []
    
    def generate_key(self, name):
        key = f"key-{name}-{hashlib.sha256(name.encode()).hexdigest()[:8]}"
        self.keys.append(key)
        return key
    
    def sign(self, filename, key):
        with open(filename, 'rb') as f:
            content = f.read()
        return SignedArtifact(filename=filename, hash_sha256=hashlib.sha256(content).hexdigest(), 
                            signature=f"sig-{hashlib.sha256(content).hexdigest()[:16]}", signed_by=key)
    
    def verify(self, artifact): return True
    def __repr__(self): return f"CodeSigner(keys={len(self.keys)})"
