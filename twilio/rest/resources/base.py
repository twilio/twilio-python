import logging
from urlparse import urlparse
from urllib import urlencode

import twilio
from twilio import TwilioException, TwilioRestException
from twilio.rest.resources.imports import parse_qs, httplib2, json
from twilio.rest.resources.util import transform_params


class Response(object):
    """
    Take a httplib2 response and turn it into a requests response
    """
    def __init__(self, httplib_resp, content, url):
        self.content = content
        self.cached = False
        self.status_code = int(httplib_resp.status)
        self.ok = self.status_code < 400
        self.url = url


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


class Resource(object):
    """A REST Resource"""

    name = "Resource"

    def __init__(self, base_uri, auth):
        self.base_uri = base_uri
        self.auth = auth

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def request(self, method, uri, **kwargs):
        """
        Send an HTTP request to the resource.

        Raise a TwilioRestException
        """
        resp = make_twilio_request(method, uri, auth=self.auth, **kwargs)

        logging.debug(resp.content)

        if method == "DELETE":
            return resp, {}
        else:
            return resp, json.loads(resp.content)

    @property
    def uri(self):
        format = (self.base_uri, self.name)
        return "%s/%s" % format


class InstanceResource(Resource):

    subresources = []
    id_key = "sid"

    def __init__(self, parent, sid):
        self.parent = parent
        self.name = sid
        super(InstanceResource, self).__init__(parent.uri,
            parent.auth)

    def load(self, entries):
        if "from" in entries.keys():
            entries["from_"] = entries["from"]
            del entries["from"]

        if "uri" in entries.keys():
            del entries["uri"]

        self.__dict__.update(entries)

    def load_subresources(self):
        """
        Load all subresources
        """
        for resource in self.subresources:
            list_resource = resource(self.uri, self.parent.auth)
            self.__dict__[list_resource.key] = list_resource

    def update_instance(self, **kwargs):
        a = self.parent.update(self.name, **kwargs)
        self.load(a.__dict__)

    def delete_instance(self):
        return self.parent.delete(self.name)


class ListResource(Resource):

    name = "Resources"
    instance = InstanceResource

    def __init__(self, *args, **kwargs):
        super(ListResource, self).__init__(*args, **kwargs)

        try:
            self.key
        except AttributeError:
            self.key = self.name.lower()

    def get(self, sid):
        """Return an instance resource"""
        return self.get_instance(sid)

    def get_instance(self, sid):
        """Request the specified instance resource"""
        uri = "%s/%s" % (self.uri, sid)
        resp, item = self.request("GET", uri)
        return self.load_instance(item)

    def get_instances(self, params):
        """
        Query the list resource for a list of InstanceResources.

        Raises a TwilioRestException if requesting a page of results that does
        not exist.

        :param dict params: List of URL parameters to be included in request
        :param int page: The page of results to retrieve (most recent at 0)
        :param int page_size: The number of results to be returned.

        :returns: -- the list of resources
        """
        params = transform_params(params)

        resp, page = self.request("GET", self.uri, params=params)

        if self.key not in page:
            raise TwilioException("Key %s not present in response" % self.key)

        return [self.load_instance(ir) for ir in page[self.key]]

    def create_instance(self, body):
        """
        Create an InstanceResource via a POST to the List Resource

        :param dict body: Dictionary of POST data
        """
        resp, instance = self.request("POST", self.uri,
                                      data=transform_params(body))

        if resp.status_code != 201:
            raise TwilioRestException(resp.status,
                                      self.uri, "Resource not created")

        return self.load_instance(instance)

    def delete_instance(self, sid):
        """
        Delete an InstanceResource via DELETE

        body: string -- HTTP Body for the quest
        """
        uri = "%s/%s" % (self.uri, sid)
        resp, instance = self.request("DELETE", uri)
        return resp.status_code == 204

    def update_instance(self, sid, body):
        """
        Update an InstanceResource via a POST

        sid: string -- String identifier for the list resource
        body: dictionary -- Dict of items to POST
        """
        uri = "%s/%s" % (self.uri, sid)
        resp, entry = self.request("POST", uri, data=transform_params(body))
        return self.load_instance(entry)

    def count(self):
        """
        Return the number of instance resources contained in this list resource
        """
        resp, page = self.request("GET", self.uri)
        return page["total"]

    def iter(self, **kwargs):
        """
        Return all instance resources using an iterator
        """
        params = transform_params(kwargs)

        while True:
            resp, page = self.request("GET", self.uri, params=params)

            if self.key not in page:
                raise StopIteration()

            for ir in page[self.key]:
                yield self.load_instance(ir)

            if not page.get('next_page_uri', ''):
                raise StopIteration()

            o = urlparse(page['next_page_uri'])
            params.update(parse_qs(o.query))

    def load_instance(self, data):
        instance = self.instance(self, data[self.instance.id_key])
        instance.load(data)
        instance.load_subresources()
        return instance
