# -*- coding:utf-8 -*-

"""Implementation of algorithm's compare two files (JSON or YAML formats)."""

from gendiff.comparator.constants import (
    STATUS,
    ADDED,
    REMOVED,
    UPDATED,
    UNCHANGED,
    UPDATED_VALUE,
    VALUE,
)


def compare(first_set, second_set):
    """Return result of compare two sets.

    Args:
        first_set {dict or set}: first set for compare
        second_set {dict or set}: second set for compare

    Returns:
        diff {dict}: result of compare two sets
    """
    diff = {}

    keys_unchanged = first_set & second_set
    for unchanged in keys_unchanged:
        diff[unchanged] = compare_value(first_set[unchanged], second_set[unchanged])

    keys_removed = first_set - second_set
    for removed in keys_removed:
        diff[removed] = {STATUS: REMOVED, VALUE: first_set[removed]}

    keys_added = second_set - first_set
    for added in keys_added:
        diff[added] = {STATUS: ADDED, VALUE: second_set[added]}

    return diff


def compare_value(first_value, second_value):
    """Return result of compare two values.

    Args:
        first_value: first value for compare
        second_value: second value for compare

    Returns:
        diff {dict} result of compare
    """
    if first_value == second_value:
        return {STATUS: UNCHANGED, VALUE: first_value}
    return {STATUS: UPDATED, VALUE: first_value, UPDATED_VALUE: second_value}
