from gi.repository.Gtk import Window, WindowType, WindowPosition, main
from gi.repository.Gdk import threads_init


from time import sleep

from zaguan.controller import WebContainerController


class Zaguan(object):
    def __init__(self, uri, controller=None):
        if controller is None:
            controller = WebContainerController()
        self.controller = controller
        self.uri = uri
        self.on_close = None

    def run(self, settings=None, window=None, debug=False, on_close=None):
        self.on_close = on_close
        threads_init()

        if window is None:
            self.window = Window(WindowType.TOPLEVEL)
            self.window.set_position(WindowPosition.CENTER_ALWAYS)
        else:
            self.window = window

        browser = self.controller.get_browser(self.uri, debug=debug,
                                              settings=settings)
        self.window.connect("delete-event", self.quit)
        self.window.set_border_width(0)
        self.window.add(browser)

        sleep(1)
        self.window.show_all()
        self.window.show()
        main()

    def quit(self, widget, event):
        if self.on_close is not None:
            self.on_close(widget, event)
