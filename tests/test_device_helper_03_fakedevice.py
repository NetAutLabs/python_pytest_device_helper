from typing import Sequence, Dict

from awesome_code.devices import DeviceType, BaseDevice
from awesome_code.device_helper import DeviceHelper

import pytest

"""
Using a fake device to avoid using mocks or patching
"""


class FakeDevice(BaseDevice):
    """
    A fake device implementation for tests
    """

    cli_responses = {
        "show user": "No user",
        "show a": "a",
        "show b": "b",
        "show c": "c",
        "do xyz": "did xyz",
    }

    # TODO: Implement (override) the methods inherited from BaseDevice.
    # Do not override the `cli` method.
    # Hint: You need to override more than one method.


@pytest.mark.xfail(reason="Implement the FakeDevice class to fix this test", run=False)
def test_device_helper_awesome_workflow_fake_device(cat9k24: DeviceType):
    dh = DeviceHelper("sw01", cat9k24, device_cls=FakeDevice)
    result = dh.awesome_workflow()

    expected_result = {
        "show user": "No user",
        "show a": "a",
        "show b": "b",
        "show c": "c",
        "do xyz": "did xyz",
    }

    assert result == expected_result
