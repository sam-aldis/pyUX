import wx
import ux.exceptions
import thread

''' 
This module handles the UI creation, if the ui module is changed (i.e from wx to tkinter or other)
then the functions should be named the same, this allows for the UI framework to easily be switched
out at a later date
'''

# THe component class can be extended/overwritten to create new elements
# Creates the basic structure for all other objects
class Component:
    def __init__(self,window):
        self.window = window

    def draw():
        pass

# Use this class to define styles so that they can be swapped for other options without forcing
# the user to change their markup
class WindowStyles:
    self.MAXIMIZE_BUTTON = wx.MAXIMIZE_BOX
    self.RESIZE_BORDER = wx.RESIZE_BORDER
    self.SYSTEM_MENU = wx.SYSTEM_MENU
    self.CAPTION = wx.CAPTION
    self.CLOSE_BUTTON = wx.CLOSE_BOX
    self.MINIMIZE_BUTTON = wx.MINIMIZE_BOX
    self.CLIP_CHILDREN = wx.CLIP_CHILDREN

class UI:
    # Initialises the UI with basic options
    def __init__(self,**kwargs):
        self.title = kwargs.get('title','')
        self.size = wx.Size(kwargs.get('size',wx.DefaultSize))
        if kwargs.get('position',False) != False
            self.position = wx.Position(kwargs.get('position'))
        else:
            self.position = wx.DefaultPosition()
        self.style = kwargs.get('style',wx.DEFAULT_FRAME_STYLE)
    # Creates the main application window for this ui
    # This should always be called
    def createWindow(self,parent=None):
        self.app = wx.App()
        self.window = wx.Window(parent, -1, self.title)
        self.window.Show()
        self.mainthread = thread.start_new(self.app.mainloop,())
    
    # Add Menu Bar
    # items passed to this function should be in an array of dictionaries
    # i.e.
    # { 'id' : wx.ID_EXIT, 'name' : 'Exit', 'help' : 'Quit the application'}
    def addMenuBar(self, *args):
        self.menuBar = we.Menu()
        for item in args:
            self.menuBar.Append(item['id'], item['name'],item['help'])

    # Adds a component to the window
    def addComponent(self,component,parent=self.window):
        parent

    # Center the window on the screen
    def centerWindow(self):
        self.window.Center()