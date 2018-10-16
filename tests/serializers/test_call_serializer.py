import json

from telephone_bill.serializers import call_serializer as srs
from telephone_bill.domain.call import Call


def test_serialize_domain_call():
    call = Call(
        destination='8899999999',
        start_date='2018-01-01',
        start_time='01:00:00',
        duration='0h1m0s',
        price=0.36)
    
    expected_json = """
{
"destination": "8899999999",
"start_date": "2018-01-01",
"start_time": "01:00:00",
"duration": "0h1m0s",
"price": 0.36
}
"""

    assert json.loads(json.dumps(call, cls=srs.CallEncoder)) == json.loads(expected_json)