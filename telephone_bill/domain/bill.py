from telephone_bill.shared.domain_model import DomainModel
from telephone_bill.domain.call import Call


class Bill:

    def __init__(self, subscriber_number, period, calls=[]):
        self.subscriber_number = subscriber_number
        self.period = period
        self.calls = []

        for call in calls:
            self.calls.append(Call.from_dict(call))

    @classmethod
    def from_dict(cls, adict):
        bill = Bill(**adict)

        return bill


DomainModel.register(Bill)
