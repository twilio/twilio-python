from tests.holodeck.base import RequestHandler


class TwilioDeck(object):

    DEFAULT_HEADERS = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        "User-Agent": "twilio-python/4.4.0 (Python 2.7.6)"
    }

    def __init__(self, holodeck):
        self.holodeck = holodeck
        self._handlers = set()

    def activate(self):
        self._handlers.add(RequestHandler('GET', '/Accounts',
                                          ('name', 'pass'), 200,
                                          headers=self.DEFAULT_HEADERS))

        for handler in self._handlers:
            self.holodeck.add(handler)

    def deactivate(self):
        for handler in self._handlers:
            self.holodeck.remove(handler)