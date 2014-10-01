from .. import InstanceResource, ListResource
from twilio.rest.resources.util import transform_params


class WorkflowStatistics(InstanceResource):
    """ A WorkflowStatistics resource """

    def __init__(self, parent):
        self.parent = parent
        super(WorkflowStatistics, self).__init__(
            parent,
            None,
        )

    def get(self, sid, **kwargs):
        """ Get a WorkflowStatistics """
        return self.parent.get(sid, **kwargs)


class WorkflowStatisticsFactory(ListResource):
    """
    WorkflowStatistics is one of the unique endpoints in the API in that it
    only has an instance representation. Here, our ListResource class acts as a
    Factory resource.
    """

    name = "Workflows"
    instance = WorkflowStatistics

    def get(self, sid, **kwargs):
        params = transform_params(kwargs)
        uri = "%s/%s" % (self.uri, sid)
        _, data = self.request("GET", uri, params=params)
        return self.load_instance(data)

    def load_instance(self, data):
        # Overridden because WorkflowStatistics instances don't contain sids
        instance = self.instance(self)
        instance.load(data)
        return instance
