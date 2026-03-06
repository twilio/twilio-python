from twilio.rest.memory.MemoryBase import MemoryBase


class Memory(MemoryBase):

    def bulk(self):
        return self.v1.bulk

    def conversation_summary(self):
        return self.v1.conversation_summaries

    def event(self):
        return self.v1.events

    def identifier(self):
        return self.v1.identifiers

    def identify_resolution_setting(self):
        return self.v1.identity_resolution_settings

    def import_(self):
        return self.v1.import_

    def lookup(self):
        return self.v1.lookup

    def observation(self):
        return self.v1.observations

    def profile(self):
        return self.v1.profiles

    def recall(self):
        return self.v1.recall

