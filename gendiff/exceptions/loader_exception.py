# -*- coding:utf-8 -*-

"""Exception  implementations for loader."""


class GendiffFileError(Exception):
    """Exception class for loader."""

    pass  # noqa: WPS420, WPS604


def invalid_extension(file_name):
    """Returns message for exception.

    If extension is wrong

    Args:
        file_name (string): file with wrong extension

    Returns:
        message (string): message with file_name
    """
    return "{0} has invalid file extension. nuse one of: .json .yaml .yml".format(
        file_name,
    )


def file_open_error(file_name):
    """Returns message for exception.

    If file not open

    Args:
        file_name (string): file with wrong extension

    Returns:
        message (string): message with file_name
    """
    return "{0}: file open error".format(file_name)


def incorrect_yaml_file(file_name):
    """Returns message for exception.

    If file YAML not correct

    Args:
        file_name (string): file with wrong extension

    Returns:
        message (string): message with file_name
    """
    return "{0}: incorrect YAML file".format(file_name)


def incorrect_json_file(file_name):
    """Returns message for exception.

    If file JSON not correct

    Args:
        file_name (string): file with wrong extension

    Returns:
        message (string): message with file_name
    """
    return "{0}: incorrect JSON file".format(file_name)
