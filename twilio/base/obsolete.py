import warnings
import functools


class ObsoleteException(BaseException):
    """ Base class for warnings about obsolete features. """
    pass


def obsolete_client(func):
    """This is a decorator which can be used to mark Client classes as
    obsolete. It will result in an error being emitted when the class is
    instantiated."""

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        raise ObsoleteException(
            "{} has been removed from this version of the library. "
            "Please refer to current documentation for guidance."
            .format(func.__name__)
        )

    return new_func
