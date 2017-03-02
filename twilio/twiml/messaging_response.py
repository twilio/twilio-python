from twilio.twiml import TwiML


class MessagingResponse(TwiML):

    def __init__(self):
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
        return self.append(Message(
            body=body,
            to=to,
            from_=from_,
            method=method,
            action=action,
            status_callback=status_callback,
            **kwargs
        ))

    def redirect(self, method=None, url=None, **kwargs):
        return self.append(Redirect(
            method=method,
            url=url,
            **kwargs
        ))


class Message(TwiML):

    def __init__(self, body=None, **kwargs):
        super(Message, self).__init__(**kwargs)
        if body:
            self.body = body

    def body(self, body):
        return self.append(Body(body))

    def media(self, url):
        return self.append(Media(url))


class Body(TwiML):
    def __init__(self, body):
        super(Body, self).__init__()
        self.body = body


class Media(TwiML):
    def __init__(self, url):
        super(Media, self).__init__()
        self.body = url


class Redirect(TwiML):
    pass

