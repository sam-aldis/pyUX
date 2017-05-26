# PARSER ERRORS - Can be used to swap out for different Locales
_EXCEPTION_FILE_NOT_SET = "No file set for the parser"
_EXCEPTION_FILE_NOT_FOUND = "The file could not be found!"
_EXCEPTION_FILE_EMPTY = "The loaded file was empty"

class ParserError(Exception):
    pass

# UI Processing Errors
_EXCEPTION_MAIN_WINDOW_NOT_FOUND = "The main window hasn't been created"
_EXCEPTION_NON_UI_OBJECT = "The object passed was not a ui object"

class UIError(Exception):
    pass