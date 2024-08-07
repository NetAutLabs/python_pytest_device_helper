import os
from typing import Dict, Type
from .devices import BaseDevice, Device, DeviceType


class DeviceHelper:
    def __init__(
        self,
        name: str,
        device_type: DeviceType,
        hostname: str = None,
        user: str = None,
        password: str = None,
        device_cls: Type[BaseDevice] = Device,
    ) -> None:
        self.name = name
        self.hostname = hostname if hostname else name
        self.user = user if user else os.getenv("USERNAME", "vendor")
        self.password = password if password else os.getenv("PASSWORD", "vendor")
        self.device_type = device_type
        self.device = device_cls(
            name=self.name,
            hostname=self.hostname,
            device_type=self.device_type,
            user=self.user,
            password=self.password,
        )

    def awesome_workflow(self) -> Dict[str, str]:
        with self.device:
            user = self.device.cli(["show user"])
            abc = self.device.cli(["show a", "show b", "show c"])
            do = self.device.cli(["do xyz"])
        return {**user, **abc, **do}
