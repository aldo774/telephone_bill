import json


class CallEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'destination': o.destination,
                'start_date': o.start_date,
                'start_time': o.start_time,
                'duration': o.duration,
                'price': o.price,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
