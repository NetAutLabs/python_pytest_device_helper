import pytest

from awesome_code.devices import PortRange, DeviceType


@pytest.fixture(scope="session")
def cat9k24_access():
    return PortRange(
        name="GigabitEthernet", stacks=[1], modules=[0], ports=range(1, 25)
    )


@pytest.fixture(scope="session")
def cat9k24_stack_ports():
    return PortRange(
        name="GigabitEthernet", stacks=range(1, 5), modules=[0], ports=range(1, 25)
    )


@pytest.fixture(scope="session")
def cat9k24_uplink():
    return PortRange(name="TenGigEthernet", stacks=[1], modules=[1], ports=range(1, 9))


@pytest.fixture(scope="session")
def cat9k24(cat9k24_access, cat9k24_uplink):
    return DeviceType(
        "C9300-24TP", access_ports=[cat9k24_access], uplink_ports=[cat9k24_uplink]
    )


@pytest.fixture(scope="session")
def cat9k48_stack():
    access_ports = [
        PortRange(
            name="GigabitEthernet", stacks=range(1, 5), modules=[0], ports=range(1, 49)
        ),
        PortRange(
            name="GigabitEthernet", stacks=range(1, 5), modules=[1], ports=range(1, 13)
        ),
    ]
    uplink_ports = [
        PortRange(
            name="TenGigEthernet", stacks=range(1, 5), modules=[1], ports=range(1, 9)
        ),
        PortRange(
            name="FortyGigabitEthernet",
            stacks=range(1, 5),
            modules=[1],
            ports=range(1, 3),
        ),
    ]
    return DeviceType(
        "C9300-48XY", access_ports=access_ports, uplink_ports=uplink_ports
    )
