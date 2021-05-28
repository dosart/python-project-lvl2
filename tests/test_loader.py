# -*- coding:utf-8 -*-

"""Tests of loader."""

import pytest

from gendiff.loader import load_data, GendiffFileError
from gendiff.loader import invalid_extension


def test_wrong_extension():
    with pytest.raises(GendiffFileError) as exception_info:
        value = load_data("tests/fixtures/wrong_extension.txt")
    assert str(exception_info.value) == invalid_extension(
        "tests/fixtures/wrong_extension.txt"
    )
