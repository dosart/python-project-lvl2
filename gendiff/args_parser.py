# -*- coding:utf-8 -*-
"""Implementation command line parser."""

import argparse

from gendiff.formaters.formater import default_format
from gendiff.formaters.formater import formats


def make_parser():
    """Return new argument parser.

    Returns:
        parser (ArgumentParser): argument parser
     """
    parser = argparse.ArgumentParser(description='Gendiff (GENerator of DIFFerences).')
    parser.add_argument('first_file', type=str, help='first file to compare')
    parser.add_argument('second_file', type=str, help='second file to compare')
    parser.add_argument('-f', '--format', type=str, choices=formats(), default=default_format(), help='set output format')

    return parser


def parse_args(parser):
    """Return command line arguments.

    Args:
        parser(ArgumentParser): argument parser

    Returns:
        args(named tuple) : comamnd line arguments
    """
    return parser.parse_args()


def first_file_path(args):
    """Return first required command line argument.

    Args:
        args(named tuple) : comamnd line arguments

    Returns:
        file path (str): first file path
    """
    return args.first_file()


def second_file_path(args):
    """Return second required command line argument.

    Args:
        args(named tuple) : comamnd line arguments

    Returns:
        file path (str): second file path
    """
    return args.second_file()


def output_format(args):
    """Return the output format of the result.

    Args:
        args(named tuple) : comamnd line arguments

    Returns:
        format (str): format of the result
    """
    return args.format()
