from v2010.account.token import (
    Token,
    Tokens as BaseTokens,
)


class Tokens(BaseTokens):

    def create(self, ttl=None, **kwargs):
        """
        Create a new Token.

        :param int ttl: The duration in seconds for which the token
            is valid, the default value is 86,400 (24 hours).
        """
        kwargs['ttl'] = ttl
        return self.create_instance(kwargs)
