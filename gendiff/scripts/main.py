# -*- coding:utf-8 -*-

from gendiff.args_parser import make_parser, first_file_path, second_file_path
from gendiff.args_parser import output_format, parse_args


def main():
    parser = make_parser()

    args = parse_args(parser)
    first = first_file_path(args)
    second = second_file_path(args)
    format = output_format(args)


if __name__ == '__main__':
    main()
