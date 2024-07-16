from twilio.http.token_manager_initializer import TokenManagerInitializer

# Dynamic import utility function
def dynamic_import(module_name, class_name):
    from importlib import import_module
    module = import_module(module_name)
    return getattr(module, class_name)

class OauthTokenBase:
    def get_oauth_token(self, domain: str, version: str, username: str, password: str):
        Domain = dynamic_import("twilio.base.domain", "Domain")
        Version = dynamic_import("twilio.base.version", "Version")
        BearerTokenHTTPClient = dynamic_import("twilio.http.bearer_token_http_client", "BearerTokenHTTPClient")
        OrgTokenManager = dynamic_import("twilio.http.orgs_token_manager", "OrgTokenManager")
        Client = dynamic_import("twilio.rest", "Client")
        try:
            orgs_token_manager = TokenManagerInitializer.get_token_manager()
            BearerTokenHTTPClient(orgs_token_manager).get_headers(Version(Domain(Client(username, password), domain), version))
            return orgs_token_manager.fetch_access_token(version=version)
        except Exception:
            orgs_token_manager = OrgTokenManager(grant_type='client_credentials',
                                                client_id=username,
                                                client_secret=password)
            BearerTokenHTTPClient(orgs_token_manager).get_headers(Version(Domain(Client(username, password), domain), version))
            return orgs_token_manager.fetch_access_token(version=Version(Domain(Client(username, password), domain), version))