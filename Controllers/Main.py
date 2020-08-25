import sys
from Models.File import *

class Main(object):

    def __init__(self, fileInput=None):
        self.fileInput = fileInput
        self.dataFile = File(self.fileInput)

    def validateFile(self):

        try:
            e = open(self.file, "r")
            if len(e.readline()) == 0:
                raise IOError

        except IOError:
            print("\nCannot open the file")
            sys.exit(0)

    def openningFile(self):
        return self.dataFile.readInput()