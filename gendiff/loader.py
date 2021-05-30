# -*- coding:utf-8 -*-

"""File loader Implementation (JSON, YAML, YML)."""

import json
import yaml
import os

from gendiff.exceptions.loader_exception import GendiffFileError
from gendiff.exceptions.loader_exception import invalid_extension
from gendiff.exceptions.loader_exception import file_open_error
from gendiff.exceptions.loader_exception import incorrect_yaml_file
from gendiff.exceptions.loader_exception import incorrect_json_file


def _switch_loader(loader_name):
    return {"json": json.load, "yaml": yaml.safe_load, "yml": yaml.safe_load}.get(
        loader_name,
        "",
    )


def load_data(file_path):
    """Load data from file.

    Args:
        file_path {string}: path to file for reading data

    Raises:
        GendiffFileError: if error of read or format's file is wrong.

    Returns:
        data {dict}: data from file
    """
    _, extension = os.path.splitext(file_path)
    loader = _switch_loader(extension)
    if not loader:
        raise GendiffFileError(invalid_extension(file_path))
    try:
        with open(file_path, "r") as input_file:
            loader(input_file)
    except OSError:
        raise GendiffFileError(file_open_error(file_path))
    except json.JSONDecodeError:
        raise GendiffFileError(incorrect_yaml_file(file_path))
    except yaml.YAMLError:
        raise GendiffFileError(incorrect_json_file(file_path))
