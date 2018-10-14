from unittest import mock

from telephone_bill.domain.bill import Bill


def test_bill_model_init():

    bill = Bill(
        subscriber_number='8899999999',
        period='2018/01',
        calls=[{
            'destination': '9993468278',
            'start_date': '2016-02-29',
            'start_time': '12:00:00',
            'duration': '02:00:00',
            'price': 11.16,
        }]
    )

    assert bill.subscriber_number == '8899999999'
    assert bill.period == '2018/01'
    assert bill.calls[0].destination == '9993468278'
    assert bill.calls[0].start_date == '2016-02-29'
    assert bill.calls[0].start_time == '12:00:00'
    assert bill.calls[0].duration == '02:00:00'
    assert bill.calls[0].price == 11.16

def test_bill_model_from_dict():
    bill = Bill.from_dict({
        'subscriber_number': '8899999999',
        'period': '2018/01',
        'calls': [{
            'destination': '9993468278',
            'start_date': '2016-02-29',
            'start_time': '12:00:00',
            'duration': '02:00:00',
            'price': 11.16,
        }]
    })

    assert bill.subscriber_number == '8899999999'
    assert bill.period == '2018/01'
    assert bill.calls[0].destination == '9993468278'
    assert bill.calls[0].start_date == '2016-02-29'
    assert bill.calls[0].start_time == '12:00:00'
    assert bill.calls[0].duration == '02:00:00'
    assert bill.calls[0].price == 11.16
