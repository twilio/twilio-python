from twilio.twiml import TwiML


class VoiceResponse(TwiML):

    def __init__(self):
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
        return self.append(Gather(
            action=action,
            method=method,
            timeout=timeout,
            finish_on_key=finish_on_key,
            num_digits=num_digits,
        ))

    def hangup(self):
        return self.append(Hangup())

    def leave(self):
        return self.append(Leave())

    def pause(self, length=None):
        return self.append(Pause(length=length))

    def play(self,
             url,
             loop=None,
             digits=None,
             **kwargs):
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
        return self.append(Redirect(url, method=method, **kwargs))

    def reject(self, reason=None, **kwargs):
        return self.append(Reject(reason=reason, **kwargs))

    def say(self,
            body,
            loop=None,
            language=None,
            voice=None,
            **kwargs):
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
    def __init__(self, number=None, **kwargs):
        super(Dial, self).__init__(**kwargs)
        if number:
            self.body = number

    def client(self,
               name,
               method=None,
               url=None,
               status_callback_event=None,
               status_callback_method=None,
               status_callback=None,
               **kwargs):
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
    def __init__(self, name, **kwargs):
        super(Client, self).__init__(**kwargs)
        self.body = name


class Conference(TwiML):
    def __init__(self, name, **kwargs):
        super(Conference, self).__init__(**kwargs)
        self.body = name


class Number(TwiML):
    def __init__(self, number, **kwargs):
        super(Number, self).__init__(**kwargs)
        self.body = number


class Queue(TwiML):
    def __init__(self, queue_name, **kwargs):
        super(Queue, self).__init__(**kwargs)
        self.body = queue_name


class Sip(TwiML):
    def __init__(self, uri, **kwargs):
        super(Sip, self).__init__(**kwargs)
        self.body = uri


class Enqueue(TwiML):
    def __init__(self, name, **kwargs):
        super(Enqueue, self).__init__(**kwargs)
        self.body = name


class Gather(TwiML):
    def __init__(self, **kwargs):
        super(Gather, self).__init__(**kwargs)

    def say(self,
            body,
            loop=None,
            language=None,
            voice=None,
            **kwargs):
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
        return self.append(Play(
            url,
            loop=loop,
            digits=digits,
            **kwargs
        ))

    def pause(self, length=None):
        return self.append(Pause(length=length))


class Pause(TwiML):
    pass


class Play(TwiML):
    def __init__(self, url, **kwargs):
        super(Play, self).__init__(**kwargs)
        self.body = url


class Say(TwiML):
    def __init__(self, body, **kwargs):
        super(Say, self).__init__(**kwargs)
        self.body = body


class Hangup(TwiML):
    pass


class Leave(TwiML):
    pass


class Record(TwiML):
    pass


class Redirect(TwiML):
    def __init__(self, url, **kwargs):
        super(Redirect, self).__init__(**kwargs)
        self.body = url


class Reject(TwiML):
    pass


class Sms(TwiML):
    def __init__(self, body, **kwargs):
        super(Sms, self).__init__(**kwargs)
        self.body = body
