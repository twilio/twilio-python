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
    def __init__(self, expression, targets, friendlyName):

        self.expression = expression
        self.targets = targets
        self.friendly_name = friendlyName

    @property
    def expression(self):
        return self.expression

    @property
    def targets(self):
        return self.targets

    @property
    def friendlyName(self):
        return self.friendly_name

    def __repr__(self):
        out = dict()
        out['expression'] = self.expression
        out['friendlyName'] = self.friendly_name
        out['target'] = self.targets
        return str(out)
