from contextlib import suppress

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

@pytest.mark.django_db
@pytest.mark.parametrize(
    'parametrized_client, expected_result',
    (
        (pytest.lazy_fixture('spj_client'), True, ),
        (pytest.lazy_fixture('client'), False, ),
        (pytest.lazy_fixture('user_client'), False, ),
    )
)
def test_create_user_in_db(
        parametrized_client,
        expected_result,
        user_form_data,
        url_create_user,
):
    """We're checking that no one, except the admin, can create a user."""
    user_count_start = User.objects.count()
    response = parametrized_client.post(url_create_user, user_form_data)
    with suppress(ObjectDoesNotExist):
        created_user = User.objects.get(username=user_form_data['username'])
    user_count_fin = User.objects.count()
    assert (('created_user' in locals()) is expected_result)
