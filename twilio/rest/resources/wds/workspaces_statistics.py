from .. import InstanceResource, ListResource
from twilio.rest.resources.util import transform_params


class WorkspaceStatistics(InstanceResource):
    """ A WorkspaceStatistics resource """

    def __init__(self, parent):
        self.parent = parent
        super(WorkspaceStatistics, self).__init__(
            parent,
            None,
        )

    def get(self, sid, **kwargs):
        """ Get a WorkspaceStatistics """
        return self.parent.get(sid, **kwargs)


class WorkspaceStatisticsFactory(ListResource):
    """
    WorkspaceStatistics is one of the unique endpoints in the API in that it
    only has an instance representation. Here, our ListResource class acts as a
    Factory resource.
    """

    name = "Statistics"
    instance = WorkspaceStatistics

    @property
    def uri(self):
        format = (self.base_uri, self.name)
        return "%s/{}/%s" % format

    def get(self, sid, **kwargs):
        params = transform_params(kwargs)
        uri = self.uri.format(sid)
        _, data = self.request("GET", uri, params=params)
        return self.load_instance(data)

    def load_instance(self, data):
        # Overridden because WorkspaceStatistics instances don't contain sids
        instance = self.instance(self)
        instance.load(data)
        return instance
