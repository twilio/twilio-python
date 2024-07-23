from threading import Lock


class BearerTokenTwilioRestClient:
    pass


class TwilioBearerTokenAuth:
    _lock = Lock()
    access_token = None
    rest_client = None
    user_agent_extensions = None
    region = None
    edge = None

    @classmethod
    def init(cls, access_token):
        with cls._lock:
            if not access_token:
                raise ValueError("Access Token cannot be null or Empty")
            if access_token != cls.access_token:
                cls.access_token = None
            cls.access_token = access_token

    @classmethod
    def get_access_token(cls):
        with cls._lock:
            return cls.access_token

    @classmethod
    def get_header_param(cls):
        with cls._lock:
            return {"Authorization": "Bearer {token}".format(token=cls.access_token)}
