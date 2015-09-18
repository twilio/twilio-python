unset = object()


def of(d):
    return {k: v for k, v in d.iteritems() if v != unset}

