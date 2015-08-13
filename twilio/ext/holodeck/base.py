import hashlib
import json
import os


class Request(object):
    def __init__(self, url, method, auth, body, headers=None):
        self.url = url
        self.method = method
        self.body = body
        self.auth = auth
        self.headers = headers

        # Normalize body to account for empty dictionaries.
        # We want empty dictionaries to be the same as
        # not passing in a body
        if not self.body:
            self.body = None

    def _to_dict(self):
        return {
            'auth': self.auth,
            'url': self.url,
            'method': self.method,
            'body': self.body,
            'headers': self.headers
        }

    def __str__(self):
        return json.dumps(self._to_dict(), sort_keys=True, indent=4)

    def __repr__(self):
        return str(self)


class RequestHandler(object):

    def __init__(self, method, url, auth, status_code,
                 content=None,
                 content_file=None,
                 headers=None,
                 params=None, data=None):
        self.method = method
        self.url = url
        self.body = params or data
        self.auth = auth
        self.headers = headers
        self.status_code = status_code
        self.content_file = content_file
        self._content = content

        # Normalize body to account for empty dictionaries.
        # We want empty dictionaries to be the same as
        # not passing in a body
        if not self.body:
            self.body = None

    @property
    def content(self):
        if not self.content_file:
            return json.dumps(self._content)

        if not self._content:
            with open(os.path.join('tests', 'resources', self.content_file)) as f:
                self._content = f.read()

        return self._content

    def can_serve(self, request):
        return 1 - self.similarity(request) < 1e-9

    def similarity(self, request):
        total = 0
        total += 1 if self.url == request.url else 0
        total += 1 if self.method == request.method else 0
        total += 1 if self.auth == request.auth else 0
        total += self._similarity_of_dicts(self.body, request.body)
        total += self._similarity_of_dicts(self.headers, request.headers)

        return float(total) / 5

    def _similarity_of_dicts(self, a, b):
        if a == b:
            return 1
        if not a or not b:
            return 0

        key_set = set()
        key_set = key_set.union(a.keys())
        key_set = key_set.union(b.keys())

        total = 0
        for k, v in a.items():
            if k in b and b[k] == v:
                total += 1

        return float(total) / len(key_set)

    def _to_dict(self):
        return {
            'url': self.url,
            'method': self.method,
            'auth': self.auth,
            'body': self.body,
            'headers': self.headers,
            'content': self._content,
            'content_file': self.content_file
        }

    def __str__(self):
        return json.dumps(self._to_dict(), sort_keys=True, indent=4)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        key = str(self).encode('utf-8')
        hash_code = int(hashlib.md5(key).hexdigest(), 16)
        return hash_code

    def __eq__(self, other):
        if not isinstance(other, RequestHandler):
            return False
        return str(self) == str(other)

