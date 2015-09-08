import logging
import platform

from ...compat import urlencode
from ...compat import urlparse
from ...compat import urlunparse

from ... import __version__
from ...exceptions import TwilioException
from ..exceptions import TwilioRestException
from .imports import parse_qs, json
from .util import (
    parse_iso_date,
    transform_params,
    UNSET_TIMEOUT,
)

logger = logging.getLogger('twilio')


def make_twilio_request(method, uri, client=None, **kwargs):
    """
    Make a request to Twilio. Throws an error

    :return: a requests-like HTTP response
    :rtype: :class:`RequestsResponse`
    :raises TwilioRestException: if the response is a 400
        or 500-level response.
    """
    headers = kwargs.get("headers", {})

    user_agent = "twilio-python/%s (Python %s)" % (
        __version__,
        platform.python_version(),
    )
    headers["User-Agent"] = user_agent
    headers["Accept-Charset"] = "utf-8"

    if method == "POST" and "Content-Type" not in headers:
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    kwargs["headers"] = headers

    if "Accept" not in headers:
        headers["Accept"] = "application/json"

    if kwargs.pop('use_json_extension', False):
        uri += ".json"

    resp = client.make_request(method, uri, **kwargs)

    if not resp.ok:
        try:
            error = json.loads(resp.content)
            code = error["code"]
            message = error["message"]
        except:
            code = None
            message = resp.content

        raise TwilioRestException(status=resp.status_code, method=method,
                                  uri=resp.url, msg=message, code=code)

    return resp


class Query(object):

    def __init__(self, client, auth, timeout):
        self.client = client
        self.auth = auth
        self.timeout = timeout

    def request(self, method, uri,
                use_json_extension=False, **kwargs):
        """
        Send an HTTP request to the resource.

        :raises: a :exc:`~twilio.TwilioRestException`
        """
        if 'timeout' not in kwargs and self.timeout is not UNSET_TIMEOUT:
            kwargs['timeout'] = self.timeout

        kwargs['use_json_extension'] = use_json_extension

        # normalize params and data
        if 'params' in kwargs and not kwargs['params']:
            del kwargs['params']
        if 'data' in kwargs and not kwargs['data']:
            del kwargs['data']

        resp = make_twilio_request(method, uri, auth=self.auth,
                                   client=self.client, **kwargs)

        if method == "DELETE":
            return resp, {}
        else:
            return resp, json.loads(resp.content)


class CreateQuery(Query):

    def __init__(self, list_instance, uri, body,
                 use_json_extension=False):
        super(CreateQuery, self).__init__(list_instance.client,
                                          list_instance.auth,
                                          list_instance.timeout)
        self.uri = uri
        self.body = body
        self.list_instance = list_instance
        self.use_json_extension = use_json_extension

    def execute(self):
        """
        Trigger a server request to create an instance.

        :return: An instance representing the created resource
        """
        resp, instance_json = self.request(
            "POST", self.uri,
            data=transform_params(self.body),
            use_json_extension=self.use_json_extension)

        if resp.status_code not in (200, 201):
            raise TwilioRestException(resp.status_code,
                                      self.uri, "Resource not created")

        return self.list_instance.load_instance(instance_json)


class UpdateQuery(Query):

    def __init__(self, list_instance, uri, body,
                 use_json_extension=False):
        super(UpdateQuery, self).__init__(list_instance.client,
                                          list_instance.auth,
                                          list_instance.timeout)
        self.uri = uri
        self.body = body
        self.list_instance = list_instance
        self.use_json_extension = use_json_extension

    def execute(self):
        """
        Trigger a server request to update an instance resource

        :raises: a :class:`~twilio.rest.RestException` on failure
        :return: A new instance representing the updated resource
        """
        resp, entry = self.request("POST", self.uri,
                                   data=transform_params(self.body),
                                   use_json_extension=self.use_json_extension)

        if resp.status_code not in (200, 201):
            raise TwilioRestException(resp.status_code,
                                      self.uri, "Resource not updated")

        return self.list_instance.load_instance(entry)


class DeleteQuery(Query):

    def __init__(self, list_instance, uri, use_json_extension=False):
        super(DeleteQuery, self).__init__(list_instance.client,
                                          list_instance.auth,
                                          list_instance.timeout)
        self.uri = uri
        self.use_json_extension = use_json_extension

    def execute(self):
        """
        Trigger a server request to delete an instance resource

        :raises: a :class:`~twilio.rest.RestException` on failure
        :return: True iff delete was successful. False otherwise
        """
        resp, instance = self.request(
            "DELETE", self.uri,
            use_json_extension=self.use_json_extension)
        return resp.status_code == 204


class GetQuery(Query):

    def __init__(self, list_instance, uri, use_json_extension=False,
                 params=None):
        super(GetQuery, self).__init__(list_instance.client,
                                       list_instance.auth,
                                       list_instance.timeout)
        self.uri = uri
        self.list_instance = list_instance
        self.use_json_extension = use_json_extension
        self.params = params

    def execute(self):
        """
        Trigger a server request to fetch an instance resource

        :raises: a :class:`~twilio.rest.RestException` on failure
        :return: The instance resource
        """
        resp = None
        response_json = None

        if self.params:
            resp, response_json = self.request(
                'GET', self.uri, params=transform_params(self.params),
                use_json_extension=self.use_json_extension)
        else:
            resp, response_json = self.request(
                'GET', self.uri, use_json_extension=self.use_json_extension)

        return self.list_instance.load_instance(response_json)


class ListQuery(Query):

    def __init__(self, list_instance, uri,
                 params, use_json_extension=False):
        super(ListQuery, self).__init__(list_instance.client,
                                        list_instance.auth,
                                        list_instance.timeout)
        self.uri = uri
        self.params = params
        self.list_instance = list_instance
        self.use_json_extension = use_json_extension

    def execute(self):
        """
        Trigger a server request to fetch a list of instances

        Raises a :exc:`~twilio.TwilioRestException` if requesting a page of
        results that does not exist.

        :return: -- A list of instances
        """
        params = transform_params(self.params)

        resp, page = self.request("GET", self.uri, params=params,
                                  use_json_extension=self.use_json_extension)

        key = self.list_instance.key

        if not key:
            # next gen resource, try and determine key from meta property
            key = page.get('meta', {}).get('key')

            if key is None:
                raise TwilioException(
                    "Unable to determine resource key from response")

        if key not in page:
            raise TwilioException("Key %s not present in response" % key)

        return [self.list_instance.load_instance(ir) for ir in page[key]]


class Resource(object):
    """A REST Resource"""

    name = "Resource"
    use_json_extension = False

    def __init__(self, client, base_uri, auth, timeout=UNSET_TIMEOUT):
        self.client = client
        self.base_uri = base_uri
        self.auth = auth
        self.timeout = timeout

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.__dict__ == other.__dict__)

    def __hash__(self):
        return hash(frozenset(self.__dict__))

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def uri(self):
        format = (self.base_uri, self.name)
        return "%s/%s" % format


class InstanceResource(Resource):
    """ The object representation of an instance response from the Twilio API

    :param parent: The parent list class for this instance resource.
        For example, the parent for a :class:`~twilio.rest.resources.Call`
        would be a :class:`~twilio.rest.resources.Calls` object.
    :type parent: :class:`~twilio.rest.resources.ListResource`
    :param str sid: The 34-character unique identifier for this instance
    """

    subresources = []
    id_key = "sid"
    use_json_extension = True

    def __init__(self, parent, sid):
        self.parent = parent
        self.name = sid
        super(InstanceResource, self).__init__(
            parent.client,
            parent.uri,
            parent.auth,
            parent.timeout
        )

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
            list_resource = resource(
                self.client,
                self.uri,
                self.parent.auth,
                self.parent.timeout
            )

            mount_name = list_resource.key
            if hasattr(list_resource, 'mount_name') and list_resource.mount_name:
                mount_name = list_resource.mount_name

            self.__dict__[mount_name] = list_resource

    def update_instance(self, data):
        """
        Update an InstanceResource via a POST

        Usage:

        .. code-block:: python

            deleted = client.messages.get('message_sid')
                .update_instance({'body': ''}).execute()
            print deleted

        :param data: dictionary -- Dict of items to POST
        """
        return self.parent.update_instance(self.name, data)

    def delete_instance(self):
        """
        Delete an InstanceResource via DELETE

        Usage:

        .. code-block:: python

            deleted = client.messages.get('message_sid')
                .delete_instance().execute()
            print deleted

        :rtype: :class:`~twilio.rest.resources.DeleteQuery`
        :returns: A query object that be executed to trigger a server request
        """
        return self.parent.delete_instance(self.name)

    def execute(self):
        """
        Trigger a server request to fetch the instance data

        Raises a :exc:`~twilio.TwilioRestException` if the requested
        instance does not exist

        :return: -- A new instance with its attributes populated
        """
        return GetQuery(self.parent, self.uri,
                        self.use_json_extension).execute()


    def __str__(self):
        return "<%s %s>" % (self.__class__.__name__, self.name[0:5])


class NextGenInstanceResource(InstanceResource):

    use_json_extension = False

    def __init__(self, *args, **kwargs):
        super(NextGenInstanceResource, self).__init__(*args, **kwargs)

    def _parse_date(self, s):
        return parse_iso_date(s)


class ListResource(Resource):

    name = "Resources"
    instance = InstanceResource
    use_json_extension = True

    def __init__(self, *args, **kwargs):
        super(ListResource, self).__init__(*args, **kwargs)

        try:
            self.key
        except AttributeError:
            self.key = self.name.lower()

    def get_instance(self, sid):
        """
        Create a placeholder for an instance resource.

        To retrieve properties on the instance resource, you must explicitly
        call execute() on the instance.

        Usage:

        .. code-block:: python

            message = client.messages.get_instance("SM1234").execute()
            print message.body

        :rtype: :class:`~twilio.rest.resources.InstanceResource`
        :returns: A shell for an instance resource
        """
        instance = self.instance(self, sid)
        instance.load_subresources()
        return instance

    def get_instances(self, params):
        """
        Query the list resource for a list of InstanceResources.

        Usage:

        .. code-block:: python

            messages = client.messages.get_instances().execute()
            print messages

        Raises a :exc:`~twilio.TwilioRestException` if requesting a page of
        results that does not exist.

        :param dict params: List of URL parameters to be included in request
        :param int page: The page of results to retrieve (most recent at 0)
        :param int page_size: The number of results to be returned.

        :rtype: :class:`~twilio.rest.resources.ListQuery`
        :returns: A query object that can be executed
            to trigger a server request
        """
        return ListQuery(self, self.uri, params,
                         self.use_json_extension)

    def create_instance(self, body):
        """
        Create an InstanceResource via a POST to the List Resource

        Usage:

        .. code-block:: python

            message = client.messages.create_instance({
                'to': '+123',
                'from': '+321',
                'body': 'hi'
            }).execute()
            print message

        :param dict body: Dictionary of POST data
        :rtype: :class:`~twilio.rest.resources.CreateQuery`
        :returns: A query object that can be executed to
            trigger a server request
        """
        return CreateQuery(self, self.uri, body,
                           self.use_json_extension)

    def delete_instance(self, sid):
        """
        Delete an InstanceResource via DELETE

        Usage:

        .. code-block:: python

            deleted = client.messages.delete_instance('message_sid').execute()
            print deleted

        :rtype: :class:`~twilio.rest.resources.DeleteQuery`
        :returns: A query object that be executed to trigger a server request
        """
        uri = "%s/%s" % (self.uri, sid)
        return DeleteQuery(self, uri, self.use_json_extension)

    def update_instance(self, sid, body):
        """
        Update an InstanceResource via a POST

        :param sid: string -- String identifier for the list resource
        :param body: dictionary -- Dict of items to POST
        """
        uri = "%s/%s" % (self.uri, sid)
        return UpdateQuery(self, uri, body,
                           self.use_json_extension)

    def iter(self, **kwargs):
        """ Return all instance resources using an iterator

        This will fetch a page of resources from the API and yield them in
        turn. When the page is exhausted, this will make a request to the API
        to retrieve the next page. Hence you may notice a pattern - the library
        will loop through 50 objects very quickly, but there will be a delay
        retrieving the 51st as the library must make another request to the API
        for resources.

        Example usage:

        .. code-block:: python

            for message in client.messages:
                print message.sid
        """
        params = transform_params(kwargs)
        query = Query(self.client, self.auth, self.timeout)

        while True:
            resp, page = query.request(
                "GET", self.uri, params=params,
                use_json_extension=self.use_json_extension)

            if self.key not in page:
                raise StopIteration()

            for ir in page[self.key]:
                yield self.load_instance(ir)

            if not page.get('next_page_uri', ''):
                raise StopIteration()

            o = urlparse(page['next_page_uri'])
            params.update(parse_qs(o.query))

    def load_instance(self, instance_json):
        instance = self.instance(self, instance_json[self.instance.id_key])
        instance.load(instance_json)
        instance.load_subresources()
        return instance

    def __str__(self):
        return '<%s>' % (self.__class__.__name__)


class NextGenListResource(ListResource):

    name = "Resources"
    instance = NextGenInstanceResource
    use_json_extension = False

    def __init__(self, *args, **kwargs):
        super(NextGenListResource, self).__init__(*args, **kwargs)

    def iter(self, **kwargs):
        """ Return all instance resources using an iterator

        This will fetch a page of resources from the API and yield them in
        turn. When the page is exhausted, this will make a request to the API
        to retrieve the next page. Hence you may notice a pattern - the library
        will loop through 50 objects very quickly, but there will be a delay
        retrieving the 51st as the library must make another request to the API
        for resources.

        Example usage:

        .. code-block:: python

            for message in client.messages:
                print message.sid
        """
        params = urlencode(transform_params(kwargs))
        parsed = urlparse(self.uri)
        url = urlunparse(parsed[:4] + (params, ) + (parsed[5], ))

        query = Query(self.client, self.auth, self.timeout)
        while True:
            resp, page = query.request(
                "GET", url,
                use_json_extension=self.use_json_extension)

            key = page.get('meta', {}).get('key')

            if key is None or key not in page:
                raise StopIteration()

            for ir in page[key]:
                yield self.load_instance(ir)

            url = page.get('meta', {}).get('next_page_url')
            if not url:
                raise StopIteration()
