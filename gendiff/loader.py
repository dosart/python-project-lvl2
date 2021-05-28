# -*- coding:utf-8 -*-

"""File loader Implementation (JSON, YAML, YML)."""

import json
import yaml
import os


class GendiffFileError(Exception):
    pass  # noqa: WPS420, WPS604


def invalid_extension(file_name):
    return '{0} has invalid file extension. nuse one of: .json .yaml .yml'.format(
        file_name
    )


def file_open_error(file_name):
    return '{0}: file open error'.format(file_name)


def incorrect_yaml_file(file_name):
    return '{0}: incorrect YAML file'.format(file_name)


def incorrect_json_file(file_name):
    return '{0}: incorrect JSON file'.format(file_name)


def switch_loader(loader_name):
    return {'json': json.load, 'yaml': yaml.safe_load, 'yml': yaml.safe_load}.get(
        loader_name, ""
    )


def load_data(path):
    _, extension = os.path.splitext(path)
    loader = switch_loader(extension)
    if not loader:
        raise GendiffFileError(invalid_extension(path))
    try:
        with open(path, 'r') as input_file:
            loader(input_file)
    except OSError:
        raise GendiffFileError(file_open_error(path))
    except json.JSONDecodeError:
        raise GendiffFileError(incorrect_yaml_file(path))
    except yaml.YAMLError:
        raise GendiffFileError(incorrect_json_file(path))
