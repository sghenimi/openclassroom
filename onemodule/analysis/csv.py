#! /usr/bin/env python3
# coding: utf-8
import os
import logging as log

log.basicConfig(level=log.DEBUG)

# critical :  un problème très serieux qui pu causé l'arret du programme, leprogramme s'arrette si jamais l'exception est levée
# ERROR : A cause d'un probleme important, le programme n'a pu réalisé une tache
# WARNING : qlq chose d'inatendue s'est produit, mais le programme continue de fonnctionner
# INFO : le programme est bien déroulé
# DEBUG : affiche des informations détaillés pour savoir en plus sur l'excecution d'une instruction


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "files", data_file)
    try:
        with open(path_to_file, "r") as ff:
            preview = ff.readline()
        log.debug("preview of csv file : {}".format(preview))
    except FileNotFoundError as e:
        log.critical(f"Hey File not found and you have a the message: {e}")


def main():
    launch_analysis("current_mps.csv")


if __name__ == "__main__":
    main()
