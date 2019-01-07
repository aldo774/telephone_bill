from datetime import datetime
from dateutil.relativedelta import relativedelta


class SubscriberBillUseCase(object):

    def _previous_month(self):
        return format(datetime.now() - relativedelta(months=1), '%m/%Y')

    def __init__(self, repo, subscriber_number, period=None):
        self.repo = repo
        self.subscriber_number = subscriber_number
        self.period = period if period else self._previous_month()

    def execute(self):
        return self.repo.get_bill(self.subscriber_number, self.period)
