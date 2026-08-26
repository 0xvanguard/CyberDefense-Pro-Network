"""Tests for DevSecOps"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.pipeline import DevSecOps, PipelineStage, SecurityGate

def test_pipeline_stage():
    assert PipelineStage.SAST.value == "sast"
    assert PipelineStage.DAST.value == "dast"
    print("✅ PipelineStage enum OK")

def test_init():
    d = DevSecOps(project_name="myapp")
    assert d.project_name == "myapp"
    assert len(d) == 0
    print("✅ DevSecOps init OK")

def test_run_gate_pass():
    d = DevSecOps()
    gate = d.run_gate("sast", findings=2, severity_breakdown={"low": 2})
    assert gate.passed is True
    print("✅ Gate pass OK")

def test_run_gate_fail():
    d = DevSecOps()
    gate = d.run_gate("sast", findings=10, severity_breakdown={"critical": 3, "high": 5})
    assert gate.passed is False
    print("✅ Gate fail OK")

def test_full_pipeline():
    d = DevSecOps()
    gates = d.run_full_pipeline()
    assert len(gates) == 8
    print(f"✅ Full pipeline: {len(gates)} stages")

def test_statistics():
    d = DevSecOps()
    d.run_gate("sast")
    d.run_gate("dast", findings=10, severity_breakdown={"critical": 1})
    stats = d.get_statistics()
    assert stats["total_gates"] == 2
    print("✅ Statistics OK")

def test_security_gate_data():
    d = DevSecOps()
    gate = d.run_gate("test", findings=5, severity_breakdown={"medium": 3, "low": 2})
    assert gate.stage == "test"
    assert gate.findings == 5
    print("✅ Security gate data OK")

if __name__ == "__main__":
    test_pipeline_stage()
    test_init()
    test_run_gate_pass()
    test_run_gate_fail()
    test_full_pipeline()
    test_statistics()
    test_security_gate_data()
    print("\n🎉 All 7 tests passed!")
