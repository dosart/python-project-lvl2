# -*- coding:utf-8 -*-

"""Tests of loader."""

import pytest

from gendiff.loader import load_data
from gendiff.exceptions.loader_exception import GendiffFileError


@pytest.mark.parametrize(
    "file_path",
    [
        ("tests/fixtures/wrong_extension.txt"),
        ("tests/fixtures/wrong_json.json"),
        ("tests/fixtures/wrong_yaml.yaml"),
        ("file_not_exists"),
    ],
)
def test_wrong_file(file_path):
    with pytest.raises(GendiffFileError):
        assert load_data(file_path)
