# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.base import TwilioClient
from twilio.rest.resources import UNSET_TIMEOUT
from twilio.rest.taskrouter.workspace import Workspaces
from workspace.activity import Activities
from workspace.event import Events
from workspace.task import Tasks
from workspace.task_queue import TaskQueues
from workspace.worker import Workers
from workspace.workflow import Workflows
from workspace.statistics import StatisticsList


class TaskrouterClient(TwilioClient):
    """
    A client for accessing the Twilio Taskrouter API.
    
    :param str account: :param str account: Your Account SID from `your
    dashboard
        <https://twilio.com/user/account>`_
    :param str timeout: :param float timeout: The socket connect and read
    timeout
        for requests to Twilio
    :param str token: :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    """

    def __init__(self, account=None, token=None,
                 base="https://taskrouter.twilio.com", version="v1",
                 timeout=UNSET_TIMEOUT, client=None, workspace_sid=None):
        super(TaskrouterClient, self).__init__(account, token, base, version, timeout, client)
        
        self.version_uri = "{}/{}".format(base, version)
        self.workspaces = Workspaces(self.client, self.version_uri, self.auth, self.timeout)
        
        if workspace_sid:
            base_instance_uri = "{}/Workspaces/{}".format(self.version_uri, workspace_sid)
            self.activities = Activities(self.client, base_instance_uri, self.auth, self.timeout)
            self.events = Events(self.client, base_instance_uri, self.auth, self.timeout)
            self.tasks = Tasks(self.client, base_instance_uri, self.auth, self.timeout)
            self.task_queues = TaskQueues(self.client, base_instance_uri, self.auth, self.timeout)
            self.workers = Workers(self.client, base_instance_uri, self.auth, self.timeout)
            self.workflows = Workflows(self.client, base_instance_uri, self.auth, self.timeout)
            self.statistics = StatisticsList(self.client, base_instance_uri, self.auth, self.timeout)
