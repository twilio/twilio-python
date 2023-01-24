from twilio.rest.bulkexports import BulkexportsBase
from warnings import warn


class Bulkexports(BulkexportsBase):

    @property
    def exports(self):
        warn('exports() is deprecated. Use v1.exports() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.exports

    @property
    def export_configuration(self):
        warn('export_configuration() is deprecated. Use v1.export_configuration() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.export_configuration



