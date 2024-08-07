import pytest

from pytest_mock import MockerFixture
from collections import ChainMap

from awesome_code.devices import Device, DeviceType
from awesome_code.device_helper import DeviceHelper

"""
Using mocker fixture (pip install pytest-mock)
"""


@pytest.mark.xfail(reason="Use pytest_mock (mocker) fix this test", run=False)
def test_device_helper_awesome_workflow_mocker(
    cat9k24: DeviceType, mocker: MockerFixture
):
    dh = DeviceHelper("sw01", cat9k24)

    # TODO: Use mocker (pytest-mock) to patch the `Device` methods. No Return value is needed

    assert dh.awesome_workflow() == {}
    mocks[0].assert_called_once
    mocks[1].assert_called_once
    assert mocks[2].call_count == 3


@pytest.mark.xfail(reason="Use pytest_mock (mocker) fix this test", run=False)
def test_device_helper_awesome_workflow_mocker_mock(
    cat9k24: DeviceType, mocker: MockerFixture
):
    cli_responses = [
        {"show user": "No user"},
        {"show a": "a", "show b": "b", "show c": "c"},
        {"do xyz": "did xyz"},
    ]

    # TODO: Use mocker (pytest-mock) to create a Mock object to replace the dh.device object.
    # Hint: You can use a Mock object within another Mock object.

    dh = DeviceHelper("sw01", cat9k24)
    dh.device = device_mock  # Device object is replaced with a Device Mock
    result = dh.awesome_workflow()

    device_mock.__enter__.assert_called_once()
    device_mock.__exit__.assert_called_once()
    calls = [
        mocker.call(["show user"]),
        mocker.call(["show a", "show b", "show c"]),
        mocker.call(["do xyz"]),
    ]
    device_mock.cli.assert_has_calls(calls)

    assert result == dict(ChainMap(*cli_responses))
