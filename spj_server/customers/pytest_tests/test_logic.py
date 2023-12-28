from http import HTTPStatus

import pytest

from customers.models import Customer

@pytest.mark.django_db
@pytest.mark.parametrize(
    'parametrized_client, status_code, count_customers',
    (
        (pytest.lazy_fixture('spj_client'), HTTPStatus.CREATED, 1, ),
        (pytest.lazy_fixture('client'), HTTPStatus.UNAUTHORIZED, 0, ),
        (pytest.lazy_fixture('user_client'), HTTPStatus.FORBIDDEN, 0, ),
    )
)
def test_add_customer(
        parametrized_client,
        status_code,
        count_customers,
        url_customer_list,
        test_customer_data
):
    response = parametrized_client.post(url_customer_list, data=test_customer_data)
    assert response.status_code == status_code
    count = Customer.objects.count()
    assert count == count_customers