#! /usr/bin/env python3
#! coding utf-8
import argparse

import analysis.csv as acsv
import analysis.xml as axml


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?"""
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    # import pdb; pdb.set_trace()
    if args.extension == "csv":
        acsv.launch_analysis("current_mps.csv")
    elif args.extension == "xml":
        axml.launch_analysis("dscan.xml")
    else:
        print("only xml and csv ")


if __name__ == "__main__":
    main()