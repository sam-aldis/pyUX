#!/usr/bin/python
import xmltodict
import os,sys
import ux.exceptions as e
import ui
import re



# PARSER VALUES AND THEIR EQUIVILENT IN pyUX

attr = re.compile(r'@[a-zA-Z0-9].*')
inner = re.compile(r'#[a-zA-Z0-9].*')
meta = re.compile(r'@\![a-z].*')

class Parser:
    def __init__(self,file):
        self.file = file

    def _extract_meta(self):
        try:
            for i in self.ui_data.items():
                

    def _begin_parse(self):
        try:
            with open(self.file) as fh:
                doc = xmltodict.parse(fh.read())
            if doc != None and doc != "":
                return doc
            else:
                raise e.ParserError(e._EXCEPTION_FILE_NOT_FOUND)
        except Exception as error:
            raise e.ParserError(error)
    ''' 
    The ShowUI function loads the file passed when the class is initiated
    and parses the UI contained within it to process through an external module
    (External so that it can be swapped out at a later date for something different if required)
    '''
    def showUI(self):
        self.ui_data = self._begin_parse()
        meta = self._extract_meta()
        for i in self.ui_data.items():
            if i[0] == "App":
                #First object is the app container
                ux = ui.pyUX(i)
                print(ux.get_attr())

    # Prints the raw parsed data
    def printRaw(self):
        print(self._begin_parse())