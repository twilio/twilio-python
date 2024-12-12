from twilio.http.token_manager import TokenManager
from twilio.rest import Client


class OrgTokenManager(TokenManager):
    """
    Orgs Token Manager
    """

    def __init__(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        code: str = None,
        redirect_uri: str = None,
        audience: str = None,
        refreshToken: str = None,
        scope: str = None,
    ):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.redirect_uri = redirect_uri
        self.audience = audience
        self.refreshToken = refreshToken
        self.scope = scope
        self.client = Client()

    def fetch_access_token(self):
        token_instance = self.client.preview_iam.v1.token.create(
            grant_type=self.grant_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            code=self.code,
            redirect_uri=self.redirect_uri,
            audience=self.audience,
            scope=self.scope,
        )
        return token_instance.access_token
