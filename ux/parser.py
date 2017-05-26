#!/usr/bin/python
import xmltodict
import os,sys
import ux.exceptions as e

class Parser:
    def __init__(self,file):
        self.file = file
    def _begin_parse(self):
        try:
            with open(self.file) as fh:
                doc = xmltodict.parse(fh.read())
            if doc != None and doc != "":
                print(doc)
            else:
                raise e.ParserError(e._EXCEPTION_FILE_NOT_FOUND)
        except Exception as error:
            raise e.ParserError(error)
    def showUI(self):
        ui_data = self._begin_parse()
        