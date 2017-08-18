import warnings
import functools


def deprecated_client(func):
    '''This is a decorator which can be used to mark Client classes
    as deprecated. It will result in an error being emitted
    when the class is instantiated.'''

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('error', DeprecationWarning)
        warnings.warn("{} has been removed from this version of the library. "
                      "Please refer to current documentation for guidance."
                      .format(func.__name__),
                      category=DeprecationWarning)
        return func(*args, **kwargs)

    return new_func
