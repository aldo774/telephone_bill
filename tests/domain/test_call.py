from telephone_bill.domain.call import Call


def test_call_model_init():
    call = Call(
        destination='8899999999',
        start_date='2018-01-01',
        start_time='01:00:00',
        duration='0h1m0s',
        price=0.36)

    assert call.destination == '8899999999'
    assert call.start_date == '2018-01-01'
    assert call.start_time == '01:00:00'
    assert call.duration == '0h1m0s'
    assert call.price == 0.36


def test_call_model_from_dict():
    call = Call.from_dict({
        'destination': '8899999999',
        'start_date': '2018-01-01',
        'start_time': '01:00:00',
        'duration': '0h1m0s',
        'price': 0.36,
    })

    assert call.destination == '8899999999'
    assert call.start_date == '2018-01-01'
    assert call.start_time == '01:00:00'
    assert call.duration == '0h1m0s'
    assert call.price == 0.36
