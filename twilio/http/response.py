class Response(object):
    """

    """
    def __init__(self, status_code, content):
        self.content = content
        self.cached = False
        self.status_code = status_code
        self.ok = self.status_code < 400
