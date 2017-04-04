from twilio.twiml import TwiML


class MessagingResponse(TwiML):
    """
    Messaging TwiML Response
    """
    def __init__(self):
        """
        Create a new <Response>
        """
        super(MessagingResponse, self).__init__()
        self.name = 'Response'

    def message(self,
                body,
                to=None,
                from_=None,
                method=None,
                action=None,
                status_callback=None,
                **kwargs):
        """
        Add a <Message> element

        :param body: body of the message
        :param to: number to send to
        :param from_: number to send from
        :param method: action HTTP method
        :param action: action URL
        :param status_callback: callback URL
        :param kwargs: other attributes
        :return: <Message> element
        """
        return self.append(Message(
            body=body,
            to=to,
            from_=from_,
            method=method,
            action=action,
            status_callback=status_callback,
            **kwargs
        ))

    def redirect(self, url, method=None, **kwargs):
        """
        Add a <Redirect> element

        :param url: URL to redirect to
        :param method: HTTP method
        :param kwargs: other attributes
        :return: <Redirect> element
        """
        return self.append(Redirect(
            method=method,
            url=url,
            **kwargs
        ))


class Message(TwiML):
    """
    <Message> element
    """
    def __init__(self, body=None, **kwargs):
        """
        Create a new <Message> element

        :param body: body of message
        :param kwargs: other attributes
        """
        super(Message, self).__init__(**kwargs)
        if body:
            self.value = body

    def body(self, body):
        """
        Add a <Body> element

        :param body: body of message
        :return: <Body> element
        """
        return self.append(Body(body))

    def media(self, url):
        """
        Add a <Media> element

        :param url: media URL
        :return: <Media> element
        """
        return self.append(Media(url))


class Body(TwiML):
    """
    <Body> element
    """
    def __init__(self, body):
        """
        Create a new <Body> element

        :param body: message body
        """
        super(Body, self).__init__()
        self.value = body


class Media(TwiML):
    """
    <Media> element
    """
    def __init__(self, url):
        """
        Create a new <Media> element

        :param url: media URL location
        """
        super(Media, self).__init__()
        self.value = url


class Redirect(TwiML):
    """
    <Redirect> element
    """
    def __init__(self, url, **kwargs):
        """
        Create a new <Redirect> element

        :param url: redirect URL location
        """
        super(Redirect, self).__init__(**kwargs)
        self.value = url

