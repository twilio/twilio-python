from .. import NextGenInstanceResource, NextGenListResource
from .statistics import Statistics


class Worker(NextGenInstanceResource):
    """
    A Worker resource
    """
    subresources = [
        Statistics
    ]

    def delete(self):
        """
        Delete a worker.
        """
        return self.parent.delete_instance(self.name)

    def update(self, **kwargs):
        """
        Update a worker.
        """
        return self.parent.update_instance(self.name, kwargs)


class Workers(NextGenListResource):
    """ A list of Worker resources """

    name = "Workers"
    instance = Worker

    def __init__(self, base_uri, auth, timeout, **kwargs):
        super(Workers, self).__init__(base_uri, auth, timeout, **kwargs)
        self.statistics = Statistics(self.uri, auth, timeout, **kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a Workflow.

        :param friendly_name: String representing user-friendly name for the
            Worker.
        :param activity_sid: A valid Activity describing the worker's initial
            state.
        :param attributes: JSON object describing this worker. For example:
            { 'email: 'Bob@foo.com', 'phone': '8675309' }. This data will be
            passed to the Assignment Callback URL whenever Work Distribution
            Service assigns a Task to this worker.
        """
        kwargs['friendly_name'] = friendly_name
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the given worker
        """
        return self.delete_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Worker` with the given parameters.

        All the parameters are describe above in :meth:`create`
        """
        return self.update_instance(sid, kwargs)
