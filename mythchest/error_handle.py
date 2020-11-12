import functools


def exception_handle(function):
    # TODO write comment and document
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(e)
            # TODO add log to alarm
            # TODO implement feature that can be extended/used by other function, after error, do things.
            raise
    return wrapper
