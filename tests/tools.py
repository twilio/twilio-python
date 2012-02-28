from mock import Mock
from __future__ import with_statement

def create_mock_json(path):
    with open(path) as f:
        resp = Mock()
        resp.content = f.read()
        return resp
