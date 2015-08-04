from .workflow_ruletarget import WorkflowRuleTarget


class WorkflowRule:

    """
    WorkflowRule represents the top level filter
    which contains a 1 or more targets

    ..attribute::expression

       The expression at the top level filter

    ..attribute::targets

       The list of targets under the filter

    ..attribute::friendlyName

       The name of the filter
    """
    _targets = list()

    def __init__(self, expression, targets, friendly_name):

        self.expression = expression
        self.targets = targets
        self.friendly_name = friendly_name

    @property
    def expression(self):
        return self.expression

    @property
    def targets(self):
        return self.targets

    @property
    def friendly_name(self):
        return self.friendly_name

    def __repr__(self):
        return str({
            'expression': self.expression,
            'friendly_name': self.friendly_name,
            'target': self.target,
        })

