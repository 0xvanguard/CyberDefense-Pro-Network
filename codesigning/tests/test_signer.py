"""Tests for CodeSigning"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.signer import CodeSigning, Signature, SigningResult

def test_init():
    cs = CodeSigning()
    assert len(cs) == 0
    print("✅ CodeSigning init OK")

def test_sign():
    cs = CodeSigning()
    result = cs.sign("abc123hash", "Developer Inc")
    assert result.signed is True
    assert result.signature.signer == "Developer Inc"
    print("✅ Sign OK")

def test_verify_signed():
    cs = CodeSigning()
    cs.sign("abc123", "Dev")
    result = cs.verify("abc123")
    assert result.verification_passed is True
    print("✅ Verify signed OK")

def test_verify_unsigned():
    cs = CodeSigning()
    result = cs.verify("unknown")
    assert result.signed is False
    assert result.verification_passed is False
    print("✅ Verify unsigned OK")

def test_signature_algorithms():
    cs = CodeSigning()
    cs.sign("h1", "A", "ECDSA-SHA256")
    sig = cs.signatures["h1"]
    assert sig.algorithm == "ECDSA-SHA256"
    print("✅ Signature algorithms OK")

def test_certificate_chain():
    cs = CodeSigning()
    cs.sign("h1", "MyOrg")
    sig = cs.signatures["h1"]
    assert len(sig.certificate_chain) == 2
    print("✅ Certificate chain OK")

def test_statistics():
    cs = CodeSigning()
    cs.sign("h1", "A")
    cs.verify("h1")
    cs.verify("unknown")
    stats = cs.get_statistics()
    assert stats["total_signatures"] == 1
    assert stats["verifications"] == 2
    print("✅ Statistics OK")

def test_multiple_signatures():
    cs = CodeSigning()
    for i in range(5):
        cs.sign(f"hash{i}", f"Signer{i}")
    assert len(cs) == 5
    print("✅ Multiple signatures OK")

if __name__ == "__main__":
    test_init()
    test_sign()
    test_verify_signed()
    test_verify_unsigned()
    test_signature_algorithms()
    test_certificate_chain()
    test_statistics()
    test_multiple_signatures()
    print("\n🎉 All 8 tests passed!")
