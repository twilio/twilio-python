#!/usr/bin/env python
from __future__ import with_statement
import re
import os

sid = "ed59a5733d2c1c1c69a83a28"


def twilio_clean(contents):
    contents = re.sub(r"([A-Z]{2}\w{8})\w{24}", r"\1%s" % sid, contents)
    contents = re.sub(r"\"[a-z0-9]{32}\"", "\"AUTHTOKEN\"", contents)
    contents = re.sub(r"\+\d{10}", r"+14158675309", contents)
    contents = re.sub(r"[0-9\- \(\)]{14}", r"(415) 867-5309", contents)
    return contents


def main():
    for f in os.listdir(os.path.abspath(os.path.dirname(__file__))):
        path, ext = os.path.splitext(f)
        if ext == ".json":
            with open(f) as g:
                contents = g.read()
            contents = twilio_clean(contents)
            with open(f, "w") as g:
                g.write(contents.strip())
                g.write("\n")


if __name__ == "__main__":
    main()
