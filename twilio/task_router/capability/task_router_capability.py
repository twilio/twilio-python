from .capability_api import CapabilityAPI

import warnings
warnings.simplefilter('always', DeprecationWarning)

TASK_ROUTER_BASE_URL = 'https://taskrouter.twilio.com'
TASK_ROUTER_BASE_EVENTS_URL = 'https://event-bridge.twilio.com/v1/wschannels'
TASK_ROUTER_VERSION = "v1"

REQUIRED = {'required': True}
OPTIONAL = {'required': False}

def deprecated(func):
	def log_warning(*args, **kwargs):
		# stacklevel = 2 makes the warning refer to the caller of the deprecation rather than the source of deprecation itself
		warnings.warn("Call to deprecated function {}.".format(func.__name__), stacklevel = 2, category = DeprecationWarning)
		return func(*args, **kwargs)
	return log_warning


class TaskRouterCapability(CapabilityAPI):
	def __init__(self, account_sid, auth_token, workspace_sid, channel_id):
		super(TaskRouterCapability, self).__init__(account_sid, auth_token, TASK_ROUTER_VERSION, channel_id)

		self.workspace_sid = workspace_sid
		self.channel_id = channel_id 
		self.base_url = TASK_ROUTER_BASE_URL + "/" + TASK_ROUTER_VERSION + "/Workspaces/" + workspace_sid

		# validate the JWT
		self.validate_jwt()

		# set up resources
		self.setup_resource()

		# add permissions to GET and POST to the event-bridge channel
		self.allow_web_sockets(channel_id)

		# add permissions to fetch the instance resource
		self.add_policy(self.resource_url, "GET", True)

	def setup_resource(self): 
		if self.channel_id[0:2] == "WS":
			self.resource_url = self.base_url
		elif self.channel_id[0:2] == "WK":
			self.resource_url = self.base_url + "/Workers/" + self.channel_id
			activity_url = self.base_url + "/Activities"
			self.allow(activity_url, "GET")
		elif self.channel_id[0:2] == "WQ":
			self.resource_url = self.base_url + "/TaskQueues/" + self.channel_id

	def allow_web_sockets(self, channel_id): 
		web_socket_url = TASK_ROUTER_BASE_EVENTS_URL + "/" + self.account_sid + "/" + self.channel_id; 
		self.policies.append(self.make_policy(web_socket_url, "GET", True)) 
		self.policies.append(self.make_policy(web_socket_url, "POST", True))

	def validate_jwt(self): 
		if self.account_sid is None or self.account_sid[0:2] != "AC":
			raise ValueError('Invalid AccountSid provided: ' + self.account_sid)
		if self.workspace_sid is None or self.workspace_sid[0:2] != "WS":
			raise ValueError('Invalid WorkspaceSid provided: ' + self.workspace_sid)
		if self.channel_id is None:
			raise ValueError('ChannelId not provided')

		prefix = self.channel_id[0:2]
		if prefix != "WS" and prefix != "WK" and prefix != "WQ":
			raise ValueError('Invalid ChannelId provided: ' + self.channel_id)

	def allow_fetch_subresources(self):	
		self.allow(self.resource_url + "/**", "GET")

	def allow_updates(self): 
		self.allow(self.resource_url, "POST")

	def allow_updates_subresources(self):
		self.allow(self.resource_url + "/**", "POST")

	def allow_delete(self):
		self.allow(self.resource_url, "DELETE")

	def allow_delete_subresources(self):
		self.allow(self.resource_url + "/**", "DELETE")

	@deprecated
	def allow_worker_fetch_attributes(self): 
		if self.channel_id[0:2] == "WK":
			self.policies.append(self.make_policy(
				self.resource_url, 
				'GET'
				)
			)
		else:
			raise ValueError("Deprecated function not applicable to non Worker")

	@deprecated
	def allow_worker_activity_updates(self):
		if self.channel_id[0:2] == "WK":
			self.policies.append(self.make_policy(
				self.resource_url, 
				'POST',
				True,
				post_filter = {'ActivitySid': REQUIRED}
				)	
			)
		else:
			raise ValueError("Deprecated function not applicable to non Worker")


	@deprecated
	def allow_task_reservation_updates(self):
		if self.channel_id[0:2] == "WK":
			tasks_url = self.base_url + "/Tasks/**"
			self.policies.append(self.make_policy(
				tasks_url, 
				'POST',
				True,
				post_filter = {'ReservationStatus': REQUIRED},
				)
			)
		else:
			raise ValueError("Deprecated function not applicable to non Worker")

	def get_resource_url(self):
		return self.resource_url

	def generate_token(self, ttl = 3600):
		task_router_attributes = {}
		task_router_attributes["account_sid"] = self.account_sid
		task_router_attributes["workspace_sid"] = self.workspace_sid
		task_router_attributes["channel"] = self.channel_id

		if self.channel_id[0:2] == "WK":
			task_router_attributes["worker_sid"] = self.channel_id
		elif self.channel_id[0:2] == "WQ":
			task_router_attributes["taskqueue_sid"] = self.channel_id

		return self._generate_token(ttl, task_router_attributes)

class TaskRouterWorkerCapability(TaskRouterCapability):
	def __init__(self, account_sid, auth_token, workspace_sid, worker_sid): 
		super(TaskRouterWorkerCapability, self).__init__(account_sid, auth_token, workspace_sid, worker_sid)
		
		self.reservations_url = self.base_url + "/Tasks/**"
		self.activity_url = self.base_url + "/Activities"

		# add permissions to fetch the list of activities and list of worker reservations
		self.allow(self.reservations_url, "GET")
		self.allow(self.activity_url, "GET")

	def setup_resource(self): 
		self.resource_url = self.base_url + "/Workers/" + self.channel_id

	def allow_activity_updates(self):
    		self.policies.append(self.make_policy(
		        self.resource_url,
		        'POST',
		        True
	    		)	
    		)
   	def allow_reservation_updates(self):
		self.policies.append(self.make_policy(
			self.reservations_url,
			'POST',
			True
			)
		)

class TaskRouterTaskQueueCapability(TaskRouterCapability):
	def __init__(self, account_sid, auth_token, workspace_sid, taskqueue_sid): 
		super(TaskRouterTaskQueueCapability, self).__init__(account_sid, auth_token, workspace_sid, taskqueue_sid)

	def setup_resource(self):
		self.resource_url = self.base_url + "/TaskQueues/" + self.channel_id


class TaskRouterWorkspaceCapability(TaskRouterCapability):
	def __init__(self, account_sid, auth_token, workspace_sid): 
		super(TaskRouterWorkspaceCapability, self).__init__(account_sid, auth_token, workspace_sid, workspace_sid)

	def setup_resource(self): 
		self.resource_url = self.base_url


