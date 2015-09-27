from twilio.compat import izip


def compare(string1, string2):
    """Compare two strings while protecting against timing attacks

    :param str string1: the first string
    :param str string2: the second string

    :returns: True if the strings are equal, False if not
    :rtype: :obj:`bool`
    """
    if len(string1) != len(string2):
        return False
    result = True
    for c1, c2 in izip(string1, string2):
        result &= c1 == c2
    return result
