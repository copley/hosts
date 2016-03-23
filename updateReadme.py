#!/usr/bin/env python

# Script by Steven Black
# https://github.com/StevenBlack
#
# This Python script will update the readme files in this repo.
#
# pylint: disable=invalid-name
# pylint: disable=bad-whitespace

import os
import platform
import re
import shutil
import string
import subprocess
import sys
import tempfile
import time
import glob
import argparse
import socket
import json

# Project Settings
BASEDIR_PATH         = os.path.dirname(os.path.realpath(__file__))
README_TEMPLATE      = os.path.join(BASEDIR_PATH, 'readme_template.md')
README_FILENAME      = 'readme.md'
README_DATA_FILENAME = "readmeData.json"

# Detecting Python 3 for version-dependent implementations
Python3 = sys.version_info >= (3,0)

def main():

    with open(README_DATA_FILENAME, 'r') as f:
       data = json.load(f)

    if Python3:
        keys = list(data.keys())
    else:
        keys = data.keys()

    keys.sort(key=cmp_keys)

    for key in keys:
        extensions = key.replace( "-", ", ")
        extensionsStr = "* Extensions: **" + extensions + "**."
        extensionsHeader = "with "+ extensions + " extensions"

        with open(os.path.join(data[key]["location"],README_FILENAME), "wt") as out:
            for line in open(README_TEMPLATE):
                line = line.replace( '@GEN_DATE@', time.strftime("%B %d %Y", time.gmtime()))
                line = line.replace( '@EXTENSIONS@', extensionsStr )
                line = line.replace( '@EXTENSIONS_HEADER@', extensionsHeader )
                line = line.replace('@NUM_ENTRIES@', "{:,}".format(data[key]["entries"]))
                out.write( line )

def cmp_keys(item):
    return item.count('-'), item

if __name__ == "__main__":
    main()