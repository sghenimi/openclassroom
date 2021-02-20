#! /usr/bin/env python3
#! coding utf-8
import argparse
import analysis.csv as acsv
import analysis.xml as axml


def main():
    acsv.launch_analysis("current_mps.csv")
    axml.launch_analysis("dscan.xml")


if __name__ == "__main__":
    main()