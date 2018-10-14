from telephone_bill.shared.domain_model import DomainModel


class Call:

    def __init__(self, destination, start_date, start_time, duration, price):
        self.destination = destination
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration
        self.price = price

    @classmethod
    def from_dict(cls, adict):
        call = Call(**adict)

        return call


DomainModel.register(Call)
