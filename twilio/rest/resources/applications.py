from v2010.account.application import (
    Application,
    Applications as BaseApplications,
)


class Applications(BaseApplications):

    def create(self, **kwargs):
        return self.create_instance(kwargs)
