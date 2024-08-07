from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Union, Literal
from time import sleep

import logging

log = logging.getLogger("device")


class NotConnected(Exception):
    pass


@dataclass
class PortRange:
    name: str
    stacks: Iterable
    modules: Iterable
    ports: Iterable

    def get_ports(self) -> List[str]:
        ports = []
        for s in self.stacks:
            for m in self.modules:
                for p in self.ports:
                    ports.append(f"{self.name}{s}/{m}/{p}")
        return ports


@dataclass
class DeviceType:
    pid: str
    access_ports: List[PortRange]
    uplink_ports: List[PortRange]

    @staticmethod
    def _get_ports(port_ranges: List[PortRange]) -> List[str]:
        ports = []
        for port in port_ranges:
            ports.extend(port.get_ports())
        return ports

    def total_access_ports(self) -> List[str]:
        return self._get_ports(self.access_ports)

    def total_uplink_ports(self) -> List[str]:
        return self._get_ports(self.uplink_ports)


class BaseDevice(ABC):
    def __init__(
        self,
        name: str,
        hostname: str,
        device_type: DeviceType,
        user: str,
        password: str,
    ) -> None:
        self.name = name
        self.hostname = hostname
        self.device_type = device_type
        self.user = user
        self.password = password

        self.connection = False

    def __enter__(self) -> BaseDevice:
        log.debug("Enter context manager")
        self.connect()
        return self

    def __exit__(self, *args, **kwargs) -> Literal[False]:
        self.close()
        log.debug("Exit context manager")
        return False

    @abstractmethod
    def connect(self) -> None: ...

    @abstractmethod
    def close(self) -> None: ...

    def cli(self, commands: Union[str, Sequence[str]]) -> Dict[str, str]:
        log.debug("Cli called with commands=%s", commands)
        if not self.connection:
            log.debug("Cli exec not possible because device is not connected")
            raise NotConnected(f"{self.name} is not connected")

        exec_commands = [commands] if isinstance(commands, str) else commands
        return self._exec_cli(exec_commands)

    @abstractmethod
    def _exec_cli(self, exec_commands: Sequence[str]) -> Dict[str, str]: ...


class Device(BaseDevice):
    def connect(self) -> None:
        """
        Simulate connecting to a device
        """
        log.info("Connecting to %s", self.hostname)
        sleep(10)
        self.connection = True
        log.info("Connected to %s", self.hostname)

    def close(self) -> None:
        """
        Simulate close the connection
        """
        log.info("Closing connection to %s", self.hostname)
        self.connection = False
        sleep(5)
        log.info("Connection to %s closed", self.hostname)

    def _exec_cli(self, commands: Sequence[str]) -> Dict[str, str]:
        result = {}
        for cmd in commands:
            log.info("Executing %s on device %s", cmd, self.name)
            response = f"We executed the command {cmd} and got an amazing replay from the device"
            result[cmd] = response
            log.debug("Response from devece %s", response)
        return result
