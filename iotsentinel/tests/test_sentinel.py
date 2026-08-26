"""Tests for IoTSentinel"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.sentinel import IoTSentinel, Device, ThreatAlert, DeviceStatus

def test_device_status():
    assert DeviceStatus.ONLINE.value == "online"
    assert DeviceStatus.COMPROMISED.value == "compromised"
    print("✅ DeviceStatus enum OK")

def test_init():
    s = IoTSentinel()
    assert len(s) == 0
    print("✅ IoTSentinel init OK")

def test_register_device():
    s = IoTSentinel()
    dev = s.register_device("Smart Light", "light", "192.168.1.10")
    assert dev.id.startswith("IOT-")
    assert dev.device_type == "light"
    print(f"✅ Register device: {dev.id}")

def test_get_device():
    s = IoTSentinel()
    dev = s.register_device("Camera", "camera", "192.168.1.20")
    got = s.get_device(dev.id)
    assert got is not None
    assert got.name == "Camera"
    print("✅ Get device OK")

def test_scan_firmware():
    s = IoTSentinel()
    dev = s.register_device("Sensor", "sensor", "10.0.0.1", firmware="1.0.0")
    alerts = s.scan_device(dev.id)
    assert len(alerts) > 0
    assert alerts[0].threat_type == "outdated_firmware"
    print("✅ Scan firmware alert OK")

def test_scan_default_creds():
    s = IoTSentinel()
    dev = s.register_device("admin Camera", "camera", "10.0.0.2")
    alerts = s.scan_device(dev.id)
    assert any(a.threat_type == "default_credentials" for a in alerts)
    print("✅ Scan default creds OK")

def test_quarantine():
    s = IoTSentinel()
    dev = s.register_device("Bad Device", "router", "10.0.0.3")
    ok = s.quarantine_device(dev.id)
    assert ok is True
    assert s.get_device(dev.id).status == "quarantined"
    print("✅ Quarantine OK")

def test_get_by_type():
    s = IoTSentinel()
    s.register_device("Light 1", "light", "1.1.1.1")
    s.register_device("Light 2", "light", "1.1.1.2")
    s.register_device("Camera 1", "camera", "1.1.1.3")
    lights = s.get_devices_by_type("light")
    assert len(lights) == 2
    print("✅ Get by type OK")

def test_statistics():
    s = IoTSentinel()
    s.register_device("A", "light", "1.1.1.1")
    s.register_device("B", "camera", "1.1.1.2")
    stats = s.get_statistics()
    assert stats["total_devices"] == 2
    assert "light" in stats["by_type"]
    print("✅ Statistics OK")

def test_multiple_devices():
    s = IoTSentinel()
    for i in range(10):
        s.register_device(f"Device {i}", "sensor", f"10.0.0.{i}")
    assert len(s) == 10
    print("✅ Multiple devices OK")

if __name__ == "__main__":
    test_device_status()
    test_init()
    test_register_device()
    test_get_device()
    test_scan_firmware()
    test_scan_default_creds()
    test_quarantine()
    test_get_by_type()
    test_statistics()
    test_multiple_devices()
    print("\n🎉 All 10 tests passed!")
