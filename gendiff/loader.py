# -*- coding:utf-8 -*-

"""File loader Implementation (JSON, YAML, YML)."""

import json
import yaml
import os

from yaml import loader


class GendiffFileError(Exception):
    pass  # noqa: WPS420, WPS604


def invalid_extension(file_name):
    return "{0} has invalid file extension. nuse one of: .json .yaml .yml".format(
        file_name
    )


def _file_open_error(file_name):
    return "{0}: file open error".format(file_name)


def _incorrect_yaml_file(file_name):
    return "{0}: incorrect YAML file".format(file_name)


def _incorrect_json_file(file_name):
    return "{0}: incorrect JSON file".format(file_name)


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
        raise GendiffFileError(_file_open_error(file_path))
    except json.JSONDecodeError:
        raise GendiffFileError(_incorrect_yaml_file(file_path))
    except yaml.YAMLError:
        raise GendiffFileError(_incorrect_json_file(file_path))
    except GendiffFileError:
        raise
