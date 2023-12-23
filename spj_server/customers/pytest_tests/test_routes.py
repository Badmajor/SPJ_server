from http import HTTPStatus

import pytest
from django.urls import reverse

@pytest.mark.parametrize(
    'parametrized_client, status_code',
    (
        (pytest.lazy_fixture('spj_client'), HTTPStatus.OK, ),
        (pytest.lazy_fixture('client'), HTTPStatus.UNAUTHORIZED, ),
        (pytest.lazy_fixture('user_client'), HTTPStatus.FORBIDDEN, ),
    )
)
def test_endpoints_availability(
        subtests,
        parametrized_client,
        status_code,
        endpoints_name_list,
):
    for name in endpoints_name_list:
        with subtests.test(
                name=name,
                status_code=status_code,
                parametrized_client=parametrized_client
        ):
            url = reverse(f'{name}-list')
            response = parametrized_client.get(url)
            assert response.status_code == status_code
