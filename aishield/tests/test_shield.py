"""Tests for AIShield"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.shield import AIShield, AttackType, AdversarialAttack, DefenseResult

def test_attack_type_enum():
    assert AttackType.FGSM.value == "fgsm"
    assert AttackType.PGD.value == "pgd"
    print("✅ AttackType enum OK")

def test_shield_init():
    s = AIShield(model_name="resnet50")
    assert s.model_name == "resnet50"
    assert len(s.detected_attacks) == 0
    print("✅ Shield init OK")

def test_detect_clean_input():
    s = AIShield()
    result = s.detect_attack([0.1, 0.2, 0.3, 0.4])
    assert result is None
    print("✅ Clean input: no attack detected")

def test_detect_adversarial():
    s = AIShield()
    adversarial = [100.0, -100.0, 50.0, -50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    result = s.detect_attack(adversarial)
    assert result is not None
    assert result.confidence > 0
    print("✅ Adversarial detected OK")

def test_defend_clean():
    s = AIShield()
    result = s.defend([0.1, 0.2, 0.3])
    assert result.defended is True
    assert result.perturbation_detected is False
    print("✅ Defend clean OK")

def test_defend_attack():
    s = AIShield()
    result = s.defend([100.0, -100.0, 50.0, -50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    assert result.perturbation_detected is True
    print("✅ Defend attack OK")

def test_certify_robustness():
    s = AIShield()
    result = s.certify_robustness([0.1, 0.2, 0.3, 0.4], epsilon=0.01)
    assert "robust" in result
    assert "robustness_ratio" in result
    print(f"✅ Certify robustness: {result['robustness_ratio']:.2f}")

def test_statistics():
    s = AIShield()
    s.detect_attack([100.0, -100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    s.defend([0.1, 0.2, 0.3])
    stats = s.get_statistics()
    assert stats["total_detections"] > 0
    print("✅ Statistics OK")

def test_multiple_attacks():
    s = AIShield()
    for _ in range(5):
        s.detect_attack([100.0, -100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    assert len(s.detected_attacks) == 5
    print("✅ Multiple attacks OK")

def test_empty_input():
    s = AIShield()
    result = s.detect_attack([])
    assert result is None
    print("✅ Empty input OK")

if __name__ == "__main__":
    test_attack_type_enum()
    test_shield_init()
    test_detect_clean_input()
    test_detect_adversarial()
    test_defend_clean()
    test_defend_attack()
    test_certify_robustness()
    test_statistics()
    test_multiple_attacks()
    test_empty_input()
    print("\n🎉 All 10 tests passed!")
