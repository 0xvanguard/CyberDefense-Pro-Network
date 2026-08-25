"""IoT-Sentinel - IoT Security Monitor"""
from dataclasses import dataclass
from typing import List

@dataclass
class IoTDevice:
    id: str
    name: str
    ip: str
    firmware: str
    vulnerabilities: int

class IoTSentinel:
    def __init__(self):
        self.devices = []
    
    def scan_network(self): 
        self.devices = [
            IoTDevice("DEV-001", "Smart Camera", "192.168.1.10", "v2.1", 2),
            IoTDevice("DEV-002", "Smart Lock", "192.168.1.11", "v1.5", 1),
        ]
        return self.devices
    
    def check_device(self, device): return {"secure": device.vulnerabilities == 0, "vulns": device.vulnerabilities}
    def add_device(self, device): self.devices.append(device)
    def __repr__(self): return f"IoTSentinel(devices={len(self.devices)})"
