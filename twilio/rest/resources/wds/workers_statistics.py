from .. import InstanceResource, ListResource
from twilio.rest.resources.util import transform_params


class WorkerStatistics(InstanceResource):
    """ A WorkerStatistics resource """

    def __init__(self, parent):
        self.parent = parent
        super(WorkerStatistics, self).__init__(
            parent,
            None,
        )

    def get(self, sid, **kwargs):
        """ Get a WorkerStatistics """
        return self.parent.get(sid, **kwargs)


class WorkerStatisticsFactory(ListResource):
    """
    WorkerStatistics is one of the unique endpoints in the API in that it only
    has an instance representation. Here, our ListResource class acts as a
    Factory resource.
    """

    name = "Workers"
    instance = WorkerStatistics

    def get(self, sid, **kwargs):
        params = transform_params(kwargs)
        uri = "%s/%s" % (self.uri, sid)
        _, data = self.request("GET", uri, params=params)
        return self.load_instance(data)

    def load_instance(self, data):
        # Overridden because WorkerStatistics instances
        # don't contain sids
        instance = self.instance(self)
        instance.load(data)
        return instance


class WorkersStatistics(InstanceResource):
    """ A list of WorkersStatistics resources """

    def __init__(self, parent):
        self.parent = parent
        super(WorkersStatistics, self).__init__(
            parent,
            None,
        )

    def get(self, **kwargs):
        """ Get a WorkersStatistics """
        return self.parent.get(**kwargs)


class WorkersStatisticsFactory(ListResource):
    """
    WorkersStatistics is one of the unique endpoints in the API in that it only
    has an instance representation. Here, our ListResource class acts as a
    Factory resource.
    """

    name = "Workers"
    instance = WorkersStatistics

    def get(self, **kwargs):
        params = transform_params(kwargs)
        _, data = self.request("GET", self.uri, params=params)
        return self.load_instance(data)

    def load_instance(self, data):
        # Overridden because WorkerStatistics instances
        # don't contain sids
        instance = self.instance(self)
        instance.load(data)
        return instance
