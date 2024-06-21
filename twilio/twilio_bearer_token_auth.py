from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class BearerTokenTwilioRestClient:
    pass


class TwilioBearerTokenAuth:
    _lock = Lock()
    access_token = None
    rest_client = None
    executor_service = None
    user_agent_extensions = None
    region = None
    edge = None
    
    @classmethod
    def init(cls, access_token):
        with cls._lock:
            if not access_token:
                raise ValueError("Access Token cannot be null or Empty")
            if access_token != cls.access_token:
                cls.invalidate()
            cls.access_token = access_token

    @classmethod
    def get_access_token(cls):
        with cls._lock:
            return cls.access_token

    @classmethod
    def get_rest_client(cls):
        with cls._lock:
            if cls.rest_client is None:
                cls.rest_client = cls.build_oauth_rest_client()
        return cls.rest_client

    @classmethod
    def get_executor_service(cls):
        with cls._lock:
            if cls.executor_service is None:
                cls.executor_service = ThreadPoolExecutor(max_workers=None)
        return cls.executor_service

    @classmethod
    def build_oauth_rest_client(cls):
        builder = BearerTokenTwilioRestClient.Builder(cls.access_token)

        if cls.user_agent_extensions is not None:
            builder.user_agent_extensions(cls.user_agent_extensions)

        builder.region(cls.region)
        builder.edge(cls.edge)

        return builder.build()