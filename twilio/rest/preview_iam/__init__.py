
from warnings import warn
from twilio.rest.preview_iam.PreviewIamBase import PreviewIamBase
from twilio.rest.preview_iam.organizations.account import AccountList
from twilio.rest.preview_iam.organizations.role_assignment import RoleAssignmentList

# from twilio.rest.preview_iam.organizations.user import UserList
from twilio.rest.preview_iam.v1.token import TokenList
from twilio.rest.preview_iam.v1.authorize import AuthorizeList


class PreviewIam(PreviewIamBase):

    @property
    def accounts(self) -> AccountList:
        return self.organizations.accounts

    @property
    def role_assignments(self) -> RoleAssignmentList:
        return self.organizations.role_assignments

    # @property
    # def users(self) -> UserList:
    #     return self.organizations.users

    @property
    def token(self) -> TokenList:
        return self.v1.token

    @property
    def authorize(self) -> AuthorizeList:
        return self.v1.authorize
