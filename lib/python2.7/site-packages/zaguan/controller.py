from json import dumps, loads
from urllib.parse import unquote

from zaguan.container import launch_browser


class WebContainerController(object):
    """Base class for the web containers of the controllers."""
    def __init__(self):
        self.processors = []

    def on_navigation_requested(self, webview, resource, request, *args):
        """This is the Callback executed each time an URI inside the webkit
        object is loaded.

        The arguments change for both webkit versions.
        For webkit1 read:
            http://lazka.github.io/pgi-docs/WebKit-3.0/classes/WebView.html#WebKit.WebView.signals.navigation_requested
        For webkit2 read:
            http://lazka.github.io/pgi-docs/WebKit2-4.0/classes/WebView.html#WebKit2.WebView.signals.resource_load_started
        """
        uri = request.get_uri()

        self.process_uri(uri)

    def process_uri(self, uri):
        """Procces the url on each processor.

        Arguments:
            uri -- the URI to process.
        """
        for processor in self.processors:
            processor(uri)

    def set_screen(self, screen, **kwargs):
        """Sends the change sreen command to the web interface."""
        self.send_command("change_screen", [screen, kwargs])

    def send_command(self, command, data=None):
        """Inyects the JS in the browser for the givven command.

        Arguments:
            command -- the command you want to send to the UI.
            data -- the data you want to send as the command argument.
        """
        json_data = dumps(data).replace("\\\"", "\\\'")
        self.send_function("run_op('%s', '%s')" % (command, json_data))

    def get_browser(self, uri, settings=None, debug=False,
                    webkit_version=None, debug_callback=None):
        """Gets the browser objects and prpare it to bo able to be used in it's
        context.

        Arguments:
            uri -- the URI of the HTML to open with the web view.
            settings -- the settings send to webkit.
            debug -- boolean to indicate if it should output debug and add
                context menu and inspector.
            webkit_version -- the webkit gtk version (1 or 2)
        """
        if settings is None:
            settings = []

        if debug and webkit_version == 1:
            settings.append(('enable-default-context-menu', True))
            settings.append(('enable-developer-extras', True))

        browser, web_send, implementation = launch_browser(
            uri, debug=debug, user_settings=settings,
            webkit_version=webkit_version, debug_callback=debug_callback)

        self.send_function = web_send
        implementation.connect(browser, self.on_navigation_requested)

        if debug and webkit_version == 1:
            self.inspector = implementation.get_inspector(browser)

        return browser

    def add_processor(self, url_word, instance=None):
        """Adds the processor to the browser."""

        def _inner(uri):
            """Processes the url and calls for the instance.

            Arguments:
                uri -- the URI to parse.
            """
            scheme, path = uri.split(':', 1)
            if scheme == "http":
                parts = path.split("/")[2:]
                if parts[0] == url_word:
                    remain = parts[1]
                elif parts[1] == url_word:
                    remain = parts[2]
                else:
                    remain = None
                if remain is not None:
                    try:
                        action, data = remain.split("?")
                    except ValueError:
                        action = remain
                        data = "null"

                    data = loads(unquote(data))
                    # search the action at the 'action controller' instance
                    # argument. if we dont find the action, we try to get it
                    # from the controller itself.
                    method = getattr(instance, action, None)
                    if method is None:
                        method = getattr(self, action, None)

                    if not method:
                        raise NotImplementedError(action)
                    return method(data)

        self.processors.append(_inner)
