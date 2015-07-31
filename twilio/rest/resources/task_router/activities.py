from twilio.rest.taskrouter.taskrouter_activity import (
    TaskrouterActivities as BaseActivities,
    TaskrouterActivity as Activity,
)

class Activities(BaseActivities):

    def create(self, friendly_name, available):
        """
        Create an Activity.
        :param friendly_name: A human-readable name for the activity, such as
            'On Call', 'Break', 'Email', etc. Must be unique in this Workspace.
            These names will be used to calculate and expose statistics about
            workers, and give you visibility into the state of each of your
            workers.
        :param available: Boolean value indicating whether the worker should be
            eligible to receive a Task when they occupy this Activity. For
            example, a call center might have an activity named 'On Call' with
            an availability set to 'false'.
        """

        return self.create_instance({'friendly_name': friendly_name,
                                     'available': available})

