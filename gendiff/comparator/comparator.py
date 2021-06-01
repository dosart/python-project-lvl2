# -*- coding:utf-8 -*-

"""Implementation of algorithm's compare two files (JSON or YAML formats)."""

from gendiff.comparator.constants import ComparatorConstants


def compare(set_one, set_two):
    diff = {}

    keys_equals = set_one & set_two
    for key in keys_equals:
        diff[key] = compare_value(set_one[key], set_two[key])

    keys_removed = et_one - set_two
    for key in keys_removed:
        diff[key] = {}
