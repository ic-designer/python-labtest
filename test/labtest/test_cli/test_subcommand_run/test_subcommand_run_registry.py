import sys

import pytest

import labtest
from labtest.labtest import main
from labtest.registry import Registry


def test_subcommand_run_name_bad(monkeypatch):
    registry = Registry(is_singleton=False)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "run", "name"])
        with pytest.raises(ValueError, match=r"Not a registered lab test: .*"):
            main(registry=registry)


def test_subcommand_run_name_good(monkeypatch):
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_subcommand_run_name_good():
        return mock_test_subcommand_run_name_good

    with monkeypatch.context() as m:
        m.setattr(
            sys,
            "argv",
            ["main", "run", f"{__file__}:mock_test_subcommand_run_name_good"],
        )
        assert main(registry=registry) is mock_test_subcommand_run_name_good


def test_subcommand_run_registry_singleton(monkeypatch):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *, is_singleton: bool = True):  # noqa: ARG003
            return registry

    monkeypatch.setattr(labtest.labtest, "Registry", MockRegistry)

    @labtest.register(registry)
    def mock_test_subcommand_run_registry_singleton():
        return mock_test_subcommand_run_registry_singleton

    with monkeypatch.context() as m:
        m.setattr(
            sys,
            "argv",
            ["main", "run", f"{__file__}:mock_test_subcommand_run_registry_singleton"],
        )
        assert main() is mock_test_subcommand_run_registry_singleton
