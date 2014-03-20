from twilio.rest.resources import (
    ListResource,
    InstanceResource,
    transform_params,
)


class CallFeedback(InstanceResource):

    def __init__(self, parent):
        self.parent = parent
        super(InstanceResource, self).__init__(
            parent.uri,
            parent.auth,
            parent.timeout,
        )


class CallFeedbackFactory(ListResource):

    """
    CallFeedback is a unique endpoint in the API in that it only
    has an instance representation, and that instance representation
    lives at the same URL you POST to to create it. Here, our
    ListResource class acts as a Factory resource.
    """

    name = "Feedback"
    instance = CallFeedback

    def create(self, **kwargs):
        """
        Create a :class:`CallFeedback` object for the parent call.

        :param int quality: The score quality. Must be an
            int between 1 and 5.
        :param list issue: A list of issues. The issue types are
            found at the CallFeedback rest docs.
        """
        return self.create_instance(kwargs)

    def get(self, **kwargs):
        """ Get the feedback for this call

         Usage:

         .. code-block:: python
            feedback = client.calls.get("CA123").feedback
            print feedback.issues

        :rtype: :class:`~twilio.rest.resources.InstanceResource`
        :raises: a :exc:`~twilio.TwilioRestException` if the request fails
        """
        params = transform_params(kwargs)
        _, data = self.request("GET", self.uri, params=params)
        return self.load_instance(data)

    def load_instance(self, data):
        # Overridden because CallFeedback instances
        # don't contain sids :(
        instance = self.instance(self)
        instance.load(data)
        return instance
