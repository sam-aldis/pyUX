from gi.repository.GLib import idle_add

def asynchronous_gtk_message(fun):
    def worker(param):
        (function, args, kwargs) = param
        function(*args, **kwargs)

    def fun2(*args, **kwargs):
        idle_add(worker, (fun, args, kwargs))

    return fun2
