import pytest
from unittest import mock

from telephone_bill.domain.bill import Bill
from telephone_bill.use_cases import subscriber_bill_use_case as uc


@pytest.fixture
def domain_bill():

    return Bill(
        subscriber_number='99988526423',
        period='2016/02',
        calls=[{
            'destination': '9993468278',
            'start_date': '2016-02-29',
            'start_time': '12:00:00',
            'duration': '02:00:00',
            'price': 11.16,
        }]
    )


def test_subscriber_bill(domain_bill):
        repo = mock.Mock()
        repo.get_bill.return_value = domain_bill

        subscriber_bill_use_case = uc.SubscriberBillUseCase(repo, 
                                                            '99988526423',
                                                            '2016/02')
        result = subscriber_bill_use_case.execute()

        repo.get_bill.assert_called_with('99988526423', '2016/02')
        assert result == domain_bill

def test_subscriber_bill_without_period(domain_bill):
    with mock.patch('telephone_bill.use_cases.subscriber_bill_use_case.'
                    'SubscriberBillUseCase._previous_month',
                    return_value='2016/02'):
        repo = mock.Mock()
        repo.get_bill.return_value = domain_bill

        subscriber_bill_use_case = uc.SubscriberBillUseCase(repo, 
                                                            '99988526423')
        result = subscriber_bill_use_case.execute()

        repo.get_bill.assert_called_with('99988526423', '2016/02')
        assert result == domain_bill
