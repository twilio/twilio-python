from .. import NextGenInstanceResource, NextGenListResource
from .statistics import Statistics


class Workspace(NextGenInstanceResource):
    """
    A Workspace resource
    """
    subresources = [
        Statistics,
    ]

    def delete(self):
        """
        Delete a workspace.
        """
        return self.parent.delete_instance(self.name)

    def update(self, **kwargs):
        """
        Update a workspace.
        """
        return self.parent.update_instance(self.name, kwargs)


class Workspaces(NextGenListResource):
    """ A list of Workspace resources """

    name = "Workspaces"
    instance = Workspace

    def create(self, friendly_name, **kwargs):
        """
        Create a Workspace.

        :param friendly_name: Human readable description of this workspace (for
            example "Customer Support" or "2014 Election Campaign").
        :param event_callback_url: If provided, the Workspace will publish
            events to this URL. You can use this to gather data for reporting.
            See Workspace Events for more information.
        :param template: One of the available template names. Will
            pre-configure this Workspace with the Workflow and Activities
            specified in the template. Currently "FIFO" is the only available
            template, which will configure Work Distribution Service with a set
            of default activities and a single queue for first-in, first-out
            distribution.
        """
        kwargs['friendly_name'] = friendly_name
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the given workspace
        """
        return self.delete_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Workspace` with the given parameters.

        All the parameters are describe above in :meth:`create`
        """
        return self.update_instance(sid, kwargs)
