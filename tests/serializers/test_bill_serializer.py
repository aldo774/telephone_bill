import json

from telephone_bill.serializers import bill_serializer as srs
from telephone_bill.domain.bill import Bill


def test_serialize_domain_bill():
    bill = Bill(
        subscriber_number='8899999999',
        period='01/2018',
        calls=[])
    
    expected_json = """
{
"subscriber_number": "8899999999",
"period": "01/2018",
"calls": []
}
"""

    assert json.loads(json.dumps(bill, cls=srs.BillEncoder)) == json.loads(expected_json)