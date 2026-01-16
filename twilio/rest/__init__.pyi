from typing import MutableMapping, Optional, Sequence

from twilio.base.client_base import ClientBase
from twilio.credential.credential_provider import CredentialProvider
from twilio.http import HttpClient

from twilio.rest.accounts import Accounts
from twilio.rest.api import Api
from twilio.rest.assistants import Assistants
from twilio.rest.bulkexports import Bulkexports
from twilio.rest.chat import Chat
from twilio.rest.content import Content
from twilio.rest.conversations import Conversations
from twilio.rest.events import Events
from twilio.rest.flex_api import FlexApi
from twilio.rest.frontline_api import FrontlineApi
from twilio.rest.iam import Iam
from twilio.rest.insights import Insights
from twilio.rest.intelligence import Intelligence
from twilio.rest.ip_messaging import IpMessaging
from twilio.rest.knowledge.KnowledgeBase import KnowledgeBase as Knowledge
from twilio.rest.lookups import Lookups
from twilio.rest.marketplace import Marketplace
from twilio.rest.messaging import Messaging
from twilio.rest.monitor import Monitor
from twilio.rest.notify import Notify
from twilio.rest.numbers import Numbers
from twilio.rest.oauth import Oauth
from twilio.rest.preview import Preview
from twilio.rest.preview_iam import PreviewIam
from twilio.rest.pricing import Pricing
from twilio.rest.proxy import Proxy
from twilio.rest.routes import Routes
from twilio.rest.serverless import Serverless
from twilio.rest.studio import Studio
from twilio.rest.supersim import Supersim
from twilio.rest.sync import Sync
from twilio.rest.taskrouter import Taskrouter
from twilio.rest.trunking import Trunking
from twilio.rest.trusthub import Trusthub
from twilio.rest.verify import Verify
from twilio.rest.video import Video
from twilio.rest.voice import Voice
from twilio.rest.wireless import Wireless


class Client(ClientBase):
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        account_sid: Optional[str] = None,
        region: Optional[str] = None,
        http_client: Optional[HttpClient] = None,
        environment: Optional[MutableMapping[str, str]] = None,
        edge: Optional[str] = None,
        user_agent_extensions: Optional[Sequence[str]] = None,
        credential_provider: Optional[CredentialProvider] = None,
    ) -> None: ...

    @property
    def accounts(self) -> Accounts: ...

    @property
    def api(self) -> Api: ...

    @property
    def assistants(self) -> Assistants: ...

    @property
    def bulkexports(self) -> Bulkexports: ...

    @property
    def chat(self) -> Chat: ...

    @property
    def content(self) -> Content: ...

    @property
    def conversations(self) -> Conversations: ...

    @property
    def events(self) -> Events: ...

    @property
    def flex_api(self) -> FlexApi: ...

    @property
    def frontline_api(self) -> FrontlineApi: ...

    @property
    def preview_iam(self) -> PreviewIam: ...

    @property
    def iam(self) -> Iam: ...

    @property
    def insights(self) -> Insights: ...

    @property
    def intelligence(self) -> Intelligence: ...

    @property
    def ip_messaging(self) -> IpMessaging: ...

    @property
    def knowledge(self) -> Knowledge: ...

    @property
    def lookups(self) -> Lookups: ...

    @property
    def marketplace(self) -> Marketplace: ...

    @property
    def messaging(self) -> Messaging: ...

    @property
    def monitor(self) -> Monitor: ...

    @property
    def notify(self) -> Notify: ...

    @property
    def numbers(self) -> Numbers: ...

    @property
    def oauth(self) -> Oauth: ...

    @property
    def preview(self) -> Preview: ...

    @property
    def pricing(self) -> Pricing: ...

    @property
    def proxy(self) -> Proxy: ...

    @property
    def routes(self) -> Routes: ...

    @property
    def serverless(self) -> Serverless: ...

    @property
    def studio(self) -> Studio: ...

    @property
    def supersim(self) -> Supersim: ...

    @property
    def sync(self) -> Sync: ...

    @property
    def taskrouter(self) -> Taskrouter: ...

    @property
    def trunking(self) -> Trunking: ...

    @property
    def trusthub(self) -> Trusthub: ...

    @property
    def verify(self) -> Verify: ...

    @property
    def video(self) -> Video: ...

    @property
    def voice(self) -> Voice: ...

    @property
    def wireless(self) -> Wireless: ...
