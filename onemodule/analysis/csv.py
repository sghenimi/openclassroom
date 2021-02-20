#! /usr/bin/env python3
# coding: utf-8
import os


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "files", data_file)
    with open(path_to_file, "r") as ff:
        preview = ff.readline()

    print("preview of csv file : {}".format(preview))


def main():
    launch_analysis("current_mps.csv")


if __name__ == "__main__":
    main()
