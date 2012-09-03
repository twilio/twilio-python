import json
from urllib import urlencode
from urlparse import urlparse

import twilio
from twilio import TwilioRestException
from twilio.rest.resources.imports import httplib2


def make_request(method, url,
    params=None, data=None, headers=None, cookies=None, files=None,
    auth=None, timeout=None, allow_redirects=False, proxies=None):
    """Sends an HTTP request Returns :class:`Response <models.Response>`

    See the requests documentation for explanation of all these parameters

    Currently proxies, files, and cookies are all ignored
    """
    http = httplib2.Http(timeout=timeout)
    http.follow_redirects = allow_redirects

    if auth is not None:
        http.add_credentials(auth[0], auth[1])

    if data is not None:
        udata = {}
        for k, v in data.iteritems():
            try:
                udata[k.encode('utf-8')] = unicode(v).encode('utf-8')
            except UnicodeDecodeError:
                udata[k.encode('utf-8')] = unicode(v, 'utf-8').encode('utf-8')
        data = urlencode(udata)

    if params is not None:
        enc_params = urlencode(params, doseq=True)
        if urlparse(url).query:
            url = '%s&%s' % (url, enc_params)
        else:
            url = '%s?%s' % (url, enc_params)

    resp, content = http.request(url, method, headers=headers, body=data)

    # Format httplib2 request as requests object
    from twilio.rest.resources.base import Response
    return Response(resp, content, url)


def make_twilio_request(method, uri, **kwargs):
    """
    Make a request to Twilio. Throws an error
    """
    headers = kwargs.get("headers", {})
    headers["User-Agent"] = "twilio-python/%s" % twilio.__version__

    if method == "POST" and "Content-Type" not in headers:
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    kwargs["headers"] = headers

    if "Accept" not in headers:
        headers["Accept"] = "application/json"
        uri = uri + ".json"

    resp = make_request(method, uri, **kwargs)

    if not resp.ok:
        try:
            error = json.loads(resp.content)
            message = "%s: %s" % (error["code"], error["message"])
        except:
            message = resp.content

        raise TwilioRestException(resp.status_code, resp.url, message)

    return resp
