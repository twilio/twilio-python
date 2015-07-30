from twilio.rest.v2010.account.queue import (
    Queue,
    Queues as BaseQueues,
)
from twilio.rest.v2010.account.queue.member import (
    Member,
    Members as BaseMembers,
)

class Members(BaseMembers):

    def dequeue(self, url, call_sid='Front', **kwargs):
        """
        Dequeues a member from the queue and have the member's call
        begin executing the TwiML document at the url.

        :param call_sid: Call sid specifying the member, if not given,
                         the member at the front of the queue will be used
        :param url: url of the TwiML document to be executed.
        """
        kwargs['url'] = url
        return self.update_instance(call_sid, kwargs)


class Queues(BaseQueues):
    instance = Queue

    def create(self, name, **kwargs):
        """ Create an :class:`Queue` with any of these optional parameters.

        :param name: A human readable description of the application,
                              with maximum length 64 characters.
        :param max_size: The limit on calls allowed into the queue (optional)
        """
        kwargs['friendly_name'] = name
        return self.create_instance(kwargs)
