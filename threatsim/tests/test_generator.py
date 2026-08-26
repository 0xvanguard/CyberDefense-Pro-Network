"""Tests for ThreatSim"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.generator import ThreatSim, Scenario, AttackVector, SimulationResult

def test_attack_vector_enum():
    assert AttackVector.PHISHING.value == "phishing"
    assert AttackVector.RANSOMWARE.value == "ransomware"
    print("✅ AttackVector enum OK")

def test_sim_init():
    sim = ThreatSim()
    assert len(sim) == 6
    print(f"✅ ThreatSim init: {len(sim)} scenarios")

def test_get_scenario():
    sim = ThreatSim()
    s = sim.get_scenario("SC-001")
    assert s is not None
    assert s.name == "Corporate Phishing Campaign"
    print("✅ Get scenario OK")

def test_get_by_vector():
    sim = ThreatSim()
    phishing = sim.get_scenarios_by_vector("phishing")
    assert len(phishing) > 0
    print(f"✅ By vector: {len(phishing)} phishing scenarios")

def test_get_by_severity():
    sim = ThreatSim()
    critical = sim.get_scenarios_by_severity("critical")
    assert len(critical) > 0
    print(f"✅ By severity: {len(critical)} critical")

def test_simulate():
    sim = ThreatSim()
    result = sim.simulate("SC-001")
    assert isinstance(result, SimulationResult)
    assert result.total_steps > 0
    print(f"✅ Simulate: {result.detections}/{result.total_steps} detected")

def test_simulate_nonexistent():
    sim = ThreatSim()
    result = sim.simulate("SC-999")
    assert result.total_steps == 0
    print("✅ Simulate nonexistent OK")

def test_generate_random():
    sim = ThreatSim()
    s = sim.generate_random()
    assert s.id.startswith("RAND-")
    print(f"✅ Random scenario: {s.id}")

def test_statistics():
    sim = ThreatSim()
    sim.simulate("SC-001")
    stats = sim.get_statistics()
    assert stats["total_scenarios"] == 6
    assert stats["simulations_run"] == 1
    print("✅ Statistics OK")

def test_scenario_to_dict():
    sim = ThreatSim()
    s = sim.get_scenario("SC-002")
    d = {"id": s.id, "name": s.name, "severity": s.severity}
    assert d["severity"] == "critical"
    print("✅ Scenario data OK")

if __name__ == "__main__":
    test_attack_vector_enum()
    test_sim_init()
    test_get_scenario()
    test_get_by_vector()
    test_get_by_severity()
    test_simulate()
    test_simulate_nonexistent()
    test_generate_random()
    test_statistics()
    test_scenario_to_dict()
    print("\n🎉 All 10 tests passed!")
