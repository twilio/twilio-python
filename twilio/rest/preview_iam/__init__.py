
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
        warn(
            "accounts is deprecated. Use organizations.accounts instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.organizations.accounts

    @property
    def role_assignments(self) -> RoleAssignmentList:
        warn(
            "role_assignments is deprecated. Use organizations.role_assignments instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.organizations.role_assignments

    # @property
    # def users(self) -> UserList:
    #     warn(
    #         "users is deprecated. Use organizations.users instead.",
    #         DeprecationWarning,
    #         stacklevel=2,
    #     )
    #     return self.organizations.users

    @property
    def token(self) -> TokenList:
        warn(
            "token is deprecated. Use v1.token instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.token

    @property
    def authorize(self) -> AuthorizeList:
        warn(
            "authorize is deprecated. Use v1.authorize instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.authorize
