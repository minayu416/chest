import functools


def exception_handle(function):
    """Exception handle decorator

    Description:
        A exception/ error handler that can be decorated on function, 
        automatic process raise exception, error and output uniform form.

    Example:
        >>> @exception_handle
        >>> def hello_world():
        >>>     print("hello world!")

    """
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
