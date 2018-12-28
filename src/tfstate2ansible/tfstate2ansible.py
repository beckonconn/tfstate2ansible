#! /usr/bin/env python3

import json
import os
from argparse import ArgumentParser


def cli_parser():
    cli = ArgumentParser()
    cli.add_argument('path',help="Location of the TF state file")
    cli.add_argument('-o','--output',help="Location of Ansible Inventory List")
    return cli

def file_ops(stateFile):
    """
    Open file and return contents
    """
    with open(stateFile, 'r') as openStateFile:
        stateFileData = openStateFile.read()
    return stateFileData

def parse_file_contents(fileData):
    """
    Take the file contents, create JSON object
    and create lists based off resource name
    """
    resources = {}
    jsonFileData = json.loads(fileData)

    for resource_items in jsonFileData['modules'][0]['resources'].items():
        prk = resource_items[0].split('.')[0]
        prn = resource_items[0].split('.')[1]
        if prk in resources.keys():
            resources[prk].append(prn)
        elif prk is not resources.keys():
            resources[prk] = []
            resources[prk].append(prn)

    return resources

def output_to_file(tfData):
    """
    Take TF state file data and save to ansible inventory
    based off resource name
    """
    curDir = os.getcwd()
    with open(f"{curDir}/inventory", 'a') as inventoryFile:
        for k in tfData.keys():
            inventoryFile.write(f"[{k}]\n")
            for i in range(len(tfData[k])):
                inventoryFile.write(f"{tfData[k][i]}\n")


if __name__ == "__main__":
    args = cli_parser().parse_args()
    fileData = file_ops(args.path)
    tfResources = parse_file_contents(fileData)
    output_to_file(tfResources)
