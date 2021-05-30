# -*- coding:utf-8 -*-

"""File loader Implementation (JSON, YAML, YML)."""

import json
import yaml
import os

from gendiff.exceptions.GendiffFileError import GendiffFileError
from gendiff.exceptions.GendiffFileError import invalid_extension
from gendiff.exceptions.GendiffFileError import file_open_error
from gendiff.exceptions.GendiffFileError import incorrect_yaml_file
from gendiff.exceptions.GendiffFileError import incorrect_json_file


def _switch_loader(loader_name):
    return {"json": json.load, "yaml": yaml.safe_load, "yml": yaml.safe_load}.get(
        loader_name,
        "",
    )


def get_loader(file_path):
    """Return loader for file.

    Function return loader for file based on file extension

    Args:
        file_path {string}: path to file for reading data

    Returns:
        loader: loader for readeng data
    """
    _, extension = os.path.splitext(file_path)
    loader = _switch_loader(extension)
    if not loader:
        raise GendiffFileError(invalid_extension(file_path))
    return loader


def load_data(file_path):
    """Load data from file.

    Args:
        file_path {string}: path to file for reading data

    Raises:
        GendiffFileError: if error of read or format's file is wrong.

    Returns:
        data {dict}: data from file
    """
    try:
        loader = get_loader(file_path)
        with open(file_path, "r") as input_file:
            loader(input_file)
    except OSError:
        raise GendiffFileError(file_open_error(file_path))
    except json.JSONDecodeError:
        raise GendiffFileError(incorrect_yaml_file(file_path))
    except yaml.YAMLError:
        raise GendiffFileError(incorrect_json_file(file_path))
    except GendiffFileError:
        raise
