from twilio.rest.resources.base import (
    NextGenInstanceResource,
    NextGenListResource,
)


class Event(NextGenInstanceResource):
    """ A taskrouter event resource """
    pass


class Events(NextGenListResource):
    name = "Events"
    instance = Event

    def list(self, **kwargs):
        """
        Returns a page of :class:`Event` resources as a list. For paging
        information see :class:`NextGenListResource`
        :param minutes: (Optional, Default=15) Definition of the interval in
                        minutes prior to now.
        :param start_date: (Optional, Default=15 minutes prior) Filter events
                            by a start date.
        :param end_date: (Optional, Default=Now) Filter events by an end date.
        :param resource_sid: (Optional) Sid of the event resource.
        :param event_type: (Optional) The type of event to filter by.
        """
        return super(Events, self).list(**kwargs)

    def get_instances(self, params):
        """
        Query the list resource for a list of InstanceResources.
        Raises a :exc:`~twilio.TwilioRestException` if requesting a page of
        results that does not exist.
        :param dict params: List of URL parameters to be included in request
        :param str page_token: Token of the page of results to retrieve
        :param int page_size: The number of results to be returned.
        :returns: -- the list of resources
        """
        return super(Events, self).get_instances(params)
