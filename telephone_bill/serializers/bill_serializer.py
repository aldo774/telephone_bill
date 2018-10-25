import json


class BillEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'subscriber_number': o.subscriber_number,
                'period': o.period,
                'calls': o.calls,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
