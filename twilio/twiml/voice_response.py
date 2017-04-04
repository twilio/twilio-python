from twilio.twiml import TwiML


class VoiceResponse(TwiML):
    """
    Voice TwiML Response
    """
    def __init__(self):
        """
        Create a new <Response>
        """
        super(VoiceResponse, self).__init__()
        self.name = 'Response'

    def dial(self,
             number,
             action=None,
             method=None,
             timeout=None,
             hangup_on_star=None,
             time_limit=None,
             caller_id=None,
             record=None,
             trim=None,
             recording_status_callback=None,
             recording_status_callback_method=None,
             **kwargs):
        """
        Create a <Dial> element

        :param number: phone number to dial
        :param action: action URL
        :param method: action HTTP method
        :param timeout: time to wait for answer
        :param hangup_on_star: hangup call on * press
        :param time_limit: max time length
        :param caller_id: caller ID to display
        :param record: record the call
        :param trim: trim the recording
        :param recording_status_callback: status callback URL
        :param recording_status_callback_method: status callback URL method
        :param kwargs: additional attributes
        :return: <Dial> element
        """
        return self.append(Dial(
            number=number,
            action=action,
            method=method,
            timeout=timeout,
            hangup_on_star=hangup_on_star,
            time_limit=time_limit,
            caller_id=caller_id,
            record=record,
            trim=trim,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            **kwargs
        ))

    def enqueue(self,
                name,
                action=None,
                method=None,
                wait_url=None,
                wait_url_method=None,
                workflow_sid=None,
                **kwargs):
        """
        Add a new <Enqueue> element

        :param name: friendly name
        :param action: action URL
        :param method: action URL method
        :param wait_url: wait URL
        :param wait_url_method: wait URL method
        :param workflow_sid: TaskRouter workflow SID
        :param kwargs: additional attributes
        :return: <Enqueue> element
        """
        return self.append(Enqueue(
            name,
            action=action,
            method=method,
            wait_url=wait_url,
            wait_url_method=wait_url_method,
            workflow_sid=workflow_sid,
            **kwargs
        ))

    def gather(self,
               action=None,
               method=None,
               timeout=None,
               finish_on_key=None,
               num_digits=None,
               **kwargs):
        """
        Add a new <Gather> element

        :param action: action URL
        :param method: action URL method
        :param timeout: time to wait while gathering input
        :param finish_on_key: finish on key press
        :param num_digits: digits to collect
        :param kwargs: additional attributes
        :return: <Gather> element
        """
        return self.append(Gather(
            action=action,
            method=method,
            timeout=timeout,
            finish_on_key=finish_on_key,
            num_digits=num_digits,
        ))

    def hangup(self):
        """
        Add a new <Hangup> element

        :return: <Hangup> element
        """
        return self.append(Hangup())

    def leave(self):
        """
        Add a new <Leave> element

        :return: <Leave> element
        """
        return self.append(Leave())

    def pause(self, length=None):
        """
        Add a new <Pause> element

        :param length: time in seconds to pause
        :return: <Pause> element
        """
        return self.append(Pause(length=length))

    def play(self,
             url,
             loop=None,
             digits=None,
             **kwargs):
        """
        Add a new <Play> element

        :param url: url to play
        :param loop: times to loop
        :param digits: play DTMF tones during a call
        :param kwargs: additional attributes
        :return: <Play> element
        """
        return self.append(Play(
            url,
            loop=loop,
            digits=digits,
            **kwargs
        ))

    def record(self,
               action=None,
               method=None,
               timeout=None,
               finish_on_key=None,
               max_length=None,
               play_beep=None,
               trim=None,
               recording_status_callback=None,
               recording_status_callback_method=None,
               transcribe=None,
               transcribe_callback=None,
               **kwargs):
        """
        Add a new <Record> element

        :param action: action URL
        :param method: action URL method
        :param timeout: timeout for recording
        :param finish_on_key: finish recording on key
        :param max_length: max length to record
        :param play_beep: play beep
        :param trim: trim the recording
        :param recording_status_callback: status callback for the recordings
        :param recording_status_callback_method: status callback method
        :param transcribe: transcribe the recording
        :param transcribe_callback: transcribe callback URL
        :param kwargs: additional attributes
        :return: <Record> element
        """
        return self.append(Record(
            action=action,
            method=method,
            timeout=timeout,
            finish_on_key=finish_on_key,
            max_length=max_length,
            play_beep=play_beep,
            trim=trim,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            transcribe=transcribe,
            transcribe_callback=transcribe_callback,
            **kwargs
        ))

    def redirect(self, url, method=None, **kwargs):
        """
        Add a <Redirect> element

        :param url: redirect url
        :param method: redirect method
        :param kwargs: additional attributes
        :return: <Redirect> element
        """
        return self.append(Redirect(url, method=method, **kwargs))

    def reject(self, reason=None, **kwargs):
        """
        Add a <Reject> element

        :param reason: rejection reason
        :param kwargs: additional attributes
        :return: <Reject> element
        """
        return self.append(Reject(reason=reason, **kwargs))

    def say(self,
            body,
            loop=None,
            language=None,
            voice=None,
            **kwargs):
        """
        Add a <Say> element

        :param body: message body
        :param loop: times to loop
        :param language: language of message
        :param voice: voice to use
        :param kwargs: additional attributes
        :return: <Say> element
        """
        return self.append(Say(
            body,
            loop=loop,
            language=language,
            voice=voice,
            **kwargs
        ))

    def sms(self,
            body,
            to=None,
            from_=None,
            method=None,
            action=None,
            status_callback=None,
            **kwargs):
        """
        Add a <Sms> element

        :param body: body of message
        :param to: to phone number
        :param from_: from phone number
        :param method: action URL method
        :param action: action URL
        :param status_callback: status callback URL
        :param kwargs: additional attributes
        :return: <Sms> element
        """
        return self.append(Sms(
            body,
            to=to,
            from_=from_,
            method=method,
            action=action,
            status_callback=status_callback,
            **kwargs
        ))


class Dial(TwiML):
    """
    <Dial> element
    """
    def __init__(self, number=None, **kwargs):
        """
        Create a new <Dial> element

        :param number: phone number to dial
        :param kwargs: additional attributes
        """
        super(Dial, self).__init__(**kwargs)
        if number:
            self.value = number

    def client(self,
               name,
               method=None,
               url=None,
               status_callback_event=None,
               status_callback_method=None,
               status_callback=None,
               **kwargs):
        """
        Add a new <Client> element

        :param name: name of client
        :param method: action URL method
        :param url: action URL
        :param status_callback_event: events to call status callback
        :param status_callback_method: status callback URL method
        :param status_callback: status callback URL
        :param kwargs: additional attributes
        :return: <Client> element
        """
        return self.append(Client(
            name,
            method=method,
            url=url,
            status_callback_event=status_callback_event,
            status_callback_method=status_callback_method,
            status_callback=status_callback,
            **kwargs
        ))

    def conference(self,
                   name,
                   muted=None,
                   start_conference_on_enter=None,
                   end_conference_on_exit=None,
                   max_participants=None,
                   beep=None,
                   record=None,
                   trim=None,
                   wait_method=None,
                   wait_url=None,
                   event_callback_url=None,
                   status_callback_event=None,
                   status_callback=None,
                   status_callback_method=None,
                   recording_status_callback=None,
                   recording_status_callback_method=None,
                   **kwargs):
        """
        Add a <Conference> element

        :param name: name of conference
        :param muted: join the conference muted
        :param start_conference_on_enter: start the conference on enter
        :param end_conference_on_exit: end the conference on exit
        :param max_participants: max number of people in conference
        :param beep: play beep when joining
        :param record: record the conference
        :param trim: trim the recording
        :param wait_method: wait URL method
        :param wait_url: wait URL to play
        :param event_callback_url: event callback URL
        :param status_callback_event: events to call status callback
        :param status_callback: status callback URL
        :param status_callback_method: status callback URL method
        :param recording_status_callback: recording status callback URL
        :param recording_status_callback_method: recording status callback URL method
        :param kwargs: additional attributes
        :return: <Conference> element
        """
        return self.append(Conference(
            name,
            start_conference_on_enter=start_conference_on_enter,
            end_conference_on_exit=end_conference_on_exit,
            max_participants=max_participants,
            beep=beep,
            record=record,
            trim=trim,
            wait_method=wait_method,
            wait_url=wait_url,
            event_callback_url=event_callback_url,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            **kwargs
        ))

    def number(self,
               number,
               send_digits=None,
               url=None,
               method=None,
               status_callback_event=None,
               status_callback=None,
               status_callback_method=None,
               **kwargs):
        """
        Add a <Number> element

        :param number: phone number to dial
        :param send_digits: play DTMF tones when the call is answered
        :param url: TwiML URL
        :param method: TwiML URL method
        :param status_callback_event: events to call status callback
        :param status_callback: status callback URL
        :param status_callback_method: status callback URL method
        :param kwargs: additional attributes
        :return: <Number> element
        """
        return self.append(Number(
            number,
            send_digits=send_digits,
            url=url,
            method=method,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            **kwargs
        ))

    def queue(self,
              queue_name,
              url=None,
              method=None,
              reservation_sid=None,
              post_work_activity_sid=None,
              **kwargs):
        """
        Add a <Queue> element

        :param queue_name: queue name
        :param url: action URL
        :param method: action URL method
        :param reservation_sid: TaskRouter reservation SID
        :param post_work_activity_sid: TaskRouter activity SID
        :param kwargs: additional attributes
        :return: <Queue> element
        """
        return self.append(Queue(
            queue_name,
            url=url,
            method=method,
            reservation_sid=reservation_sid,
            post_work_activity_sid=post_work_activity_sid,
            **kwargs
        ))

    def sip(self,
            uri,
            username=None,
            password=None,
            url=None,
            method=None,
            status_callback_event=None,
            status_callback=None,
            status_callback_method=None,
            **kwargs):
        """
        Add a <Sip> element

        :param uri: sip url
        :param username: sip username
        :param password: sip password
        :param url: action URL
        :param method: action URL method
        :param status_callback_event: events to call status callback
        :param status_callback: status callback URL
        :param status_callback_method: status callback URL method
        :param kwargs: additional attributes
        :return: <Sip> element
        """
        return self.append(Sip(
            uri,
            username=username,
            password=password,
            url=url,
            method=method,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            **kwargs
        ))


class Client(TwiML):
    """
    <Client> element
    """
    def __init__(self, name, **kwargs):
        """
        Create a new <Client> element

        :param name: name of client
        :param kwargs: attributes
        """
        super(Client, self).__init__(**kwargs)
        self.value = name


class Conference(TwiML):
    """
    <Conference> element
    """
    def __init__(self, name, **kwargs):
        """
        Create a new <Conference> element

        :param name: name of conference
        :param kwargs: attributes
        """
        super(Conference, self).__init__(**kwargs)
        self.value = name


class Number(TwiML):
    """
    <Number> element
    """
    def __init__(self, number, **kwargs):
        """
        Create a new <Number> element

        :param number: phone number
        :param kwargs: attributes
        """
        super(Number, self).__init__(**kwargs)
        self.value = number


class Queue(TwiML):
    """
    <Queue> element
    """
    def __init__(self, queue_name, **kwargs):
        """
        Create a new <Queue> element

        :param queue_name: name of queue
        :param kwargs: attributes
        """
        super(Queue, self).__init__(**kwargs)
        self.value = queue_name


class Sip(TwiML):
    """
    <Sip> element
    """
    def __init__(self, uri, **kwargs):
        """
        Create a new <Sip> element

        :param uri: sip url
        :param kwargs: attributes
        """
        super(Sip, self).__init__(**kwargs)
        self.value = uri


class Enqueue(TwiML):
    """
    <Enqueue> element
    """
    def __init__(self, name, **kwargs):
        """
        Create a new <Enqueue> element

        :param name: queue name
        :param kwargs: attributes
        """
        super(Enqueue, self).__init__(**kwargs)
        self.value = name


class Gather(TwiML):
    """
    <Gather> element
    """
    def __init__(self, **kwargs):
        """
        Create a new <Gather> element
        :param kwargs: attributes
        """
        super(Gather, self).__init__(**kwargs)

    def say(self,
            body,
            loop=None,
            language=None,
            voice=None,
            **kwargs):
        """
        Add a new <Say> element

        :param body: message body
        :param loop: times to loop
        :param language: message language
        :param voice: voice to use
        :param kwargs: additional attributes
        :return: <Say> element
        """
        return self.append(Say(
            body,
            loop=loop,
            language=language,
            voice=voice,
            **kwargs
        ))

    def play(self,
             url,
             loop=None,
             digits=None,
             **kwargs):
        """
        Add a new <Play> element

        :param url: media URL
        :param loop: times to loop
        :param digits: digits to simulate
        :param kwargs: additional attributes
        :return: <Play> element
        """
        return self.append(Play(
            url,
            loop=loop,
            digits=digits,
            **kwargs
        ))

    def pause(self, length=None):
        """
        Add a new <Pause> element

        :param length: time to pause
        :return: <Pause> element
        """
        return self.append(Pause(length=length))


class Pause(TwiML):
    """
    <Pause> element
    """
    pass


class Play(TwiML):
    """
    <Play> element
    """
    def __init__(self, url, **kwargs):
        """
        Create a new <Play> element

        :param url: media URL
        :param kwargs: additional attributes
        """
        super(Play, self).__init__(**kwargs)
        self.value = url


class Say(TwiML):
    """
    <Say> element
    """
    def __init__(self, body, **kwargs):
        """
        Create a new <Say> element

        :param body: message body
        :param kwargs: attributes
        """
        super(Say, self).__init__(**kwargs)
        self.value = body


class Hangup(TwiML):
    """
    <Hangup> element
    """
    pass


class Leave(TwiML):
    """
    <Leave> element
    """
    pass


class Record(TwiML):
    """
    <Record> element
    """
    pass


class Redirect(TwiML):
    """
    <Redirect> element
    """
    def __init__(self, url, **kwargs):
        """
        Create a new <Redirect> element

        :param url: TwiML URL
        :param kwargs: attributes
        """
        super(Redirect, self).__init__(**kwargs)
        self.value = url


class Reject(TwiML):
    """
    <Reject> element
    """
    pass


class Sms(TwiML):
    """
    <Sms> element
    """
    def __init__(self, body, **kwargs):
        """
        Create a new <Sms> element

        :param body: message body
        :param kwargs: attributes
        """
        super(Sms, self).__init__(**kwargs)
        self.value = body
