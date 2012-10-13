from twilio.rest.resources import InstanceResource, ListResource


class UsageRecord(InstanceResource):
    """ A usage record resource """


class UsageRecords(ListResource):
    name = "Usage/Records"
    instance = UsageRecord
    key = "usage_records"

    def list(self, **kwargs):
        """
        Returns a page of :class:`UsageRecord` resources as a list. For paging
        information see :class:`ListResource`

        :param category: Only include usage of this usage category.
        :param start_date: Only include usage that has occurred on or after
                           this date. Format is YYYY-MM-DD. All dates are in
                           GMT.
        :param end_date: Only include usage that has occurred on or before this
                         date. Format is YYYY-MM-DD. All dates are in GMT.
        """
        return self.get_instances(kwargs)

    def get(self, *args, **kwargs):
        raise AttributeError('Unsupported in UsageRecords')

    def load_instance(self, data):
        instance = self.instance(self, "Resource")
        instance.load(data)
        instance.load_subresources()
        return instance
