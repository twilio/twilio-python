from twilio.rest.knowledge.KnowledgeBase import KnowledgeBase
from twilio.rest.knowledge.v1.knowledge import KnowledgeList as V1KnowledgeList
from twilio.rest.knowledge.v2.chunk import ChunkList
from twilio.rest.knowledge.v2.knowledge import KnowledgeList as V2KnowledgeList
from twilio.rest.knowledge.v2.knowledge_basis import KnowledgeBasisList
from twilio.rest.knowledge.v2.search import SearchList


class Knowledge(KnowledgeBase):
    @property
    def knowledge(self) -> V1KnowledgeList:
        return self.v1.knowledge

    @property
    def chunks(self) -> ChunkList:
        return self.v2.chunks

    @property
    def knowledge_v2(self) -> V2KnowledgeList:
        return self.v2.knowledge

    @property
    def knowledge_bases(self) -> KnowledgeBasisList:
        return self.v2.knowledge_bases

    def search(self, kb_id: str) -> SearchList:
        return self.v2.search(kb_id)
