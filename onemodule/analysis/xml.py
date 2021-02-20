#! /usr/bin/env python3
# coding: utf-8
import os


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "files", data_file)
    with open(path_to_file, "r") as ff:
        preview = ff.readline()

    print("preview of xml file : {}".format(preview))


def main():
    launch_analysis("dscan.xml")


if __name__ == "__main__":
    main()