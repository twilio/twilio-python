from twilio.base.version import Version


class ListResource:
    def __init__(self, version: Version):
        self._version = version
