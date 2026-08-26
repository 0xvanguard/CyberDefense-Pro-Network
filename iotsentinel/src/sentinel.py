"""IoTSentinel — IoT Device Security Monitoring"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum

class DeviceStatus(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    COMPROMISED = "compromised"
    QUARANTINED = "quarantined"

@dataclass
class Device:
    id: str
    name: str
    device_type: str
    ip: str
    firmware_version: str
    status: str = "online"
    vulnerabilities: int = 0
    last_seen: str = ""

    def __post_init__(self):
        if not self.last_seen:
            self.last_seen = datetime.now().isoformat()

@dataclass
class ThreatAlert:
    device_id: str
    threat_type: str
    severity: str
    description: str
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()

class IoTSentinel:
    def __init__(self):
        self.devices: Dict[str, Device] = {}
        self.alerts: List[ThreatAlert] = []
        self.device_counter = 0

    def register_device(self, name: str, device_type: str, ip: str, firmware: str = "1.0") -> Device:
        self.device_counter += 1
        device = Device(id=f"IOT-{self.device_counter:04d}", name=name, device_type=device_type,
                       ip=ip, firmware_version=firmware)
        self.devices[device.id] = device
        return device

    def get_device(self, device_id: str) -> Optional[Device]:
        return self.devices.get(device_id)

    def scan_device(self, device_id: str) -> List[ThreatAlert]:
        device = self.devices.get(device_id)
        if not device:
            return []
        alerts = []
        if device.firmware_version.startswith("1."):
            alert = ThreatAlert(device_id=device_id, threat_type="outdated_firmware",
                              severity="medium", description=f"Firmware {device.firmware_version} is outdated")
            alerts.append(alert)
            device.vulnerabilities += 1
        if device.device_type == "camera" and "admin" in device.name.lower():
            alert = ThreatAlert(device_id=device_id, threat_type="default_credentials",
                              severity="critical", description="Possible default credentials")
            alerts.append(alert)
            device.vulnerabilities += 2
        self.alerts.extend(alerts)
        return alerts

    def quarantine_device(self, device_id: str) -> bool:
        device = self.devices.get(device_id)
        if device:
            device.status = "quarantined"
            return True
        return False

    def get_devices_by_type(self, device_type: str) -> List[Device]:
        return [d for d in self.devices.values() if d.device_type == device_type]

    def get_statistics(self) -> Dict:
        types = {}
        for d in self.devices.values():
            types[d.device_type] = types.get(d.device_type, 0) + 1
        return {"total_devices": len(self.devices), "total_alerts": len(self.alerts), "by_type": types}

    def __len__(self) -> int:
        return len(self.devices)

    def __repr__(self) -> str:
        return f"IoTSentinel(devices={len(self.devices)})"
