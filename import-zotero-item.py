#!/usr/local/bin/python3

import csv
from string import Template
import sys
import textwrap

class SubscriptableDictReader:
    def __init__(self, reader):
        self.reader = reader
        self.rows = []
        for row in self.reader:
          self.rows.append(row)

    def __getitem__(self, field):
        return self.rows[0][field]

class App:
    def __init__(self, argv):
        self.checkArgv(argv)
        self.parseArgv(argv)
        self.template = Template(textwrap.dedent("""\
            ---
            Title: $Title
            Author: $Author
            URL: $Url
            DOI: $DOI
            ---
            
        """))

    def checkArgv(self, argv):
        if (len(argv) != 2):
            raise IndexError('This script requires exactly one argument')
    
    def parseArgv(self, argv):
        self.inputFilePath = argv[1]

    def execute(self):
        with open(self.inputFilePath, newline='') as inputFile:
            reader = csv.DictReader(inputFile)
            print(self.template.substitute(SubscriptableDictReader(reader)))

if __name__ == "__main__":
   App(sys.argv).execute()
