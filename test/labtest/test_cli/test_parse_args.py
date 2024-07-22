import pytest

from labtest.labtest import parse_args


def test_parse_args_command_missing(capsys):
    with pytest.raises(SystemExit) as e:
        parse_args([])
    captured = capsys.readouterr()
    assert "the following arguments are required:" in captured.err
    assert e.value.code == 2


def test_parse_args_command_bad(capsys):
    with pytest.raises(SystemExit) as e:
        parse_args(["bad"])
    captured = capsys.readouterr()
    assert "invalid choice:" in captured.err
    assert e.value.code == 2


def test_parse_args_help_run():
    with pytest.raises(SystemExit) as e:
        parse_args(["run", "-h"])
    assert e.value.code == 0


def test_parse_args_help_list():
    with pytest.raises(SystemExit) as e:
        parse_args(["list", "-h"])
    assert e.value.code == 0
