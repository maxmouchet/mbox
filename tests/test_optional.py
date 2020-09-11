import json

import pytest

from mtoolbox.optional import tryfunc, unwrap


def test_tryfunc():
    f = tryfunc(json.loads)
    assert f("[invalid") == None
    assert f('{"a": 1}') == {"a": 1}

    f = tryfunc(json.loads, default="")
    assert f("[invalid") == ""

    def raise_kb():
        raise KeyboardInterrupt()

    f = tryfunc(raise_kb)
    with pytest.raises(KeyboardInterrupt):
        f()


def test_unwrap():
    with pytest.raises(ValueError):
        unwrap(None)
    assert unwrap(True)
