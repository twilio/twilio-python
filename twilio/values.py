from six import iteritems
unset = object()


def of(d):
    return {k: v for k, v in iteritems(d) if v != unset}

