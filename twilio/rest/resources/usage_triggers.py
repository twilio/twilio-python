from twilio.rest.resources import InstanceResource, ListResource


class UsageTrigger(InstanceResource):
    """ A usage trigger resource """

    def update(self, **kwargs):
        """
        Update this usage trigger
        """
        return self.parent.update(self.sid, **kwargs)

    def delete(self):
        """
        Delete this usage trigger
        """
        return self.parent.delete(self.sid)


class UsageTriggers(ListResource):
    name = "Usage/Triggers"
    instance = UsageTrigger
    key = "usage_triggers"

    def list(self, **kwargs):
        """
        Returns a page of :class:`UsageTrigger` resources as a list. For paging
        information see :class:`ListResource`

        :param recurring: Only show UsageTriggers that count over this
                          interval. One of daily, monthly, or yearly. To
                          retrieve non-recurring triggers, leave this empty or
                          use alltime.
        :param usage_category: Only show UsageTriggers that watch this usage
                               category. Must be one of the supported usage
                               categories.
        :trigger_by: Only show UsageTriggers that trigger by this field in the
                     UsageRecord. Must be one of: count, usage, or price as
                     described in the UsageRecords documentation.
        """
        return self.get_instances(kwargs)

    def create(self, **kwargs):
        """
        Create an :class:`Application` with any of these optional parameters.

        :param friendly_name: A human readable description of the application,
                              with maximum length 64 characters.
        :param usage_category: The trigger will watch this usage category.
        :param trigger_value: The trigger will fire when usage reaches this
                              value.
        :param callback_url: Twilio will make a request to this url when the
                             trigger fires.
        :param trigger_by: The field in the UsageRecord that will fire the
                           trigger. One of count, usage, or price as described
                           in the UsageRecords documentation. The default is
                           usage.
        :param recurring: The interval the trigger will count over. Must be one
                          of: daily, monthly, or yearly. Omit this to create a
                          non-recurring trigger.
        :param callback_method: Twilio will use this HTTP method when making a
                                request to the CallbackUrl. GET or POST. The
                                default is POST.
        """
        return self.create_instance(kwargs)
