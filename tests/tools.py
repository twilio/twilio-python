from __future__ import with_statement
from mock import Mock


def create_mock_json(path):
    with open(path) as f:
        resp = Mock()
        resp.content = f.read()
        return resp
