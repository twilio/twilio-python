class WorkflowRuleTarget:
    """
    Workflow Rule target which is encompassed
    inside targets

    ..attribute::queue

      The queue which will handle the task matching this filter target

    ..attribute::expression

       The dynamic expression if any for this matching

    ..attribute::priority

      The priority for the target

    ..attribute::timeout

      The timeout before the reservation expires.
    """
    def __init__(self, queue, expression=None, priority=None, timeout=None):

        self.queue = queue
        if expression is not None:
            self.expression = expression
        if priority is not None:
            self.priority = priority
        if timeout is not None:
            self.timeout = timeout
