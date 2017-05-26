from zaguan.engines import get_wk_implementation
from zaguan.functions import asynchronous_gtk_message


def launch_browser(uri, debug=False, user_settings=None, window=None,
                   webkit_version=None, debug_callback=None):
    """Creates and initialize a browser object.

    Arguments:
        debug -- boolean to indicate if it should output debug info.
        user_settings -- dictionary with the user settings to send to webkit
        window -- a GTK window object to add the browser to.
        webkit_version -- the webkit gtk version (1 or 2)
    """
    implementation = get_wk_implementation(webkit_version)

    browser = implementation.create_browser(debug)
    implementation.set_settings(browser, user_settings)

    implementation.open_uri(browser, uri)

    def _web_send(msg):
        """Inyect some javascript anynchronously in the web view.

        Arguments:
            msg -- the javascript to run in the client;
        """
        if debug:
            if debug_callback is None:
                msg_len = 80
                print('>>>', msg[:msg_len],
                      "..." if len(msg) > msg_len else "")
            else:
                debug_callback(msg)

        func = asynchronous_gtk_message(implementation.inject_javascript)
        func(browser, msg)

    return browser, _web_send, implementation
