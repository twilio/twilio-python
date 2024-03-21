from twilio.base.version import Version


class InstanceResource:
    def __init__(self, version: Version):
        self._version = version
