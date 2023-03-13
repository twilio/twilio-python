"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsQuestionnairesQuestionList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsQuestionnairesQuestionList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionList
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Insights/QM/Questions'.format(**self._solution)
        
        
    
    
    
    def create(self, category_id, question, description, answer_set_id, allow_na, token=values.unset):
        """
        Create the InsightsQuestionnairesQuestionInstance

        :param str category_id: The ID of the category
        :param str question: The question.
        :param str description: The description for the question.
        :param str answer_set_id: The answer_set for the question.
        :param bool allow_na: The flag to enable for disable NA for answer.
        :param str token: The Token HTTP request header
        
        :returns: The created InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        data = values.of({ 
            'CategoryId': category_id,
            'Question': question,
            'Description': description,
            'AnswerSetId': answer_set_id,
            'AllowNa': allow_na,
        })
        headers = values.of({'Token': token, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsQuestionnairesQuestionInstance(self._version, payload)
    
    
    def stream(self, token=values.unset, category_id=values.unset, limit=None, page_size=None):
        """
        Streams InsightsQuestionnairesQuestionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str token: The Token HTTP request header
        :param list[str] category_id: The list of category IDs
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            token=token,
            category_id=category_id,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, token=values.unset, category_id=values.unset, limit=None, page_size=None):
        """
        Lists InsightsQuestionnairesQuestionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str token: The Token HTTP request header
        :param list[str] category_id: The list of category IDs
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance]
        """
        return list(self.stream(
            token=token,
            category_id=category_id,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, token=values.unset, category_id=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InsightsQuestionnairesQuestionInstance records from the API.
        Request is executed immediately
        
        :param str token: The Token HTTP request header
        :param list[str] category_id: The list of category IDs
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        """
        data = values.of({ 
            'Token': token,
            'CategoryId': serialize.map(category_id, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InsightsQuestionnairesQuestionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InsightsQuestionnairesQuestionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InsightsQuestionnairesQuestionPage(self._version, response, self._solution)


    def get(self, question_id):
        """
        Constructs a InsightsQuestionnairesQuestionContext
        
        :param question_id: The unique ID of the question
        
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        return InsightsQuestionnairesQuestionContext(self._version, question_id=question_id)

    def __call__(self, question_id):
        """
        Constructs a InsightsQuestionnairesQuestionContext
        
        :param question_id: The unique ID of the question
        
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        return InsightsQuestionnairesQuestionContext(self._version, question_id=question_id)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionList>'








class InsightsQuestionnairesQuestionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InsightsQuestionnairesQuestionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InsightsQuestionnairesQuestionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        return InsightsQuestionnairesQuestionInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionPage>'




class InsightsQuestionnairesQuestionInstance(InstanceResource):

    def __init__(self, version, payload, question_id: str=None):
        """
        Initialize the InsightsQuestionnairesQuestionInstance
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'question_id': payload.get('question_id'),
            'question': payload.get('question'),
            'description': payload.get('description'),
            'category': payload.get('category'),
            'answer_set_id': payload.get('answer_set_id'),
            'allow_na': payload.get('allow_na'),
            'usage': deserialize.integer(payload.get('usage')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'question_id': question_id or self._properties['question_id'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsQuestionnairesQuestionContext for this InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        if self._context is None:
            self._context = InsightsQuestionnairesQuestionContext(self._version, question_id=self._solution['question_id'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def question_id(self):
        """
        :returns: The unique ID of the question
        :rtype: str
        """
        return self._properties['question_id']
    
    @property
    def question(self):
        """
        :returns: The question.
        :rtype: str
        """
        return self._properties['question']
    
    @property
    def description(self):
        """
        :returns: The description for the question.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def category(self):
        """
        :returns: The Category for the question.
        :rtype: dict
        """
        return self._properties['category']
    
    @property
    def answer_set_id(self):
        """
        :returns: The answer_set for the question.
        :rtype: str
        """
        return self._properties['answer_set_id']
    
    @property
    def allow_na(self):
        """
        :returns: The flag  to enable for disable NA for answer.
        :rtype: bool
        """
        return self._properties['allow_na']
    
    @property
    def usage(self):
        """
        :returns: Integer value that tells a particular question is used by how many questionnaires
        :rtype: int
        """
        return self._properties['usage']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesQuestionInstance
        
        :params str token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(token=token, )
    
    def update(self, allow_na, token=values.unset, category_id=values.unset, question=values.unset, description=values.unset, answer_set_id=values.unset):
        """
        Update the InsightsQuestionnairesQuestionInstance
        
        :params bool allow_na: The flag to enable for disable NA for answer.
        :params str token: The Token HTTP request header
        :params str category_id: The ID of the category
        :params str question: The question.
        :params str description: The description for the question.
        :params str answer_set_id: The answer_set for the question.

        :returns: The updated InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        return self._proxy.update(allow_na=allow_na, token=token, category_id=category_id, question=question, description=description, answer_set_id=answer_set_id, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionInstance {}>'.format(context)

class InsightsQuestionnairesQuestionContext(InstanceContext):

    def __init__(self, version: Version, question_id: str):
        """
        Initialize the InsightsQuestionnairesQuestionContext

        :param Version version: Version that contains the resource
        :param question_id: The unique ID of the question

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'question_id': question_id,
        }
        self._uri = '/Insights/QM/Questions/{question_id}'.format(**self._solution)
        
    
    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesQuestionInstance

        :param str token: The Token HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'Token': token, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def update(self, allow_na, token=values.unset, category_id=values.unset, question=values.unset, description=values.unset, answer_set_id=values.unset):
        """
        Update the InsightsQuestionnairesQuestionInstance
        
        :params bool allow_na: The flag to enable for disable NA for answer.
        :params str token: The Token HTTP request header
        :params str category_id: The ID of the category
        :params str question: The question.
        :params str description: The description for the question.
        :params str answer_set_id: The answer_set for the question.

        :returns: The updated InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        data = values.of({ 
            'AllowNa': allow_na,
            'CategoryId': category_id,
            'Question': question,
            'Description': description,
            'AnswerSetId': answer_set_id,
        })
        headers = values.of({'Token': token, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsQuestionnairesQuestionInstance(
            self._version,
            payload,
            question_id=self._solution['question_id']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionContext {}>'.format(context)


