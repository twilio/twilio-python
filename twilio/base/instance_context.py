from twilio.base.version import Version


class InstanceContext:
    def __init__(self, version: Version):
        self._version = version
