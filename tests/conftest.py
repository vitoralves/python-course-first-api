from venv import create
import pytest
from flask_jwt_extended import create_access_token
from app import create_app


@pytest.fixture(scope='module')
def get_headers():
    token = create_access_token(identity='user_test')
    return {
        'Authorization': 'Bearer {}'.format(token)
    }


@pytest.fixture(scope='module')
def test_client():
    client = create_app()

    with client.test_client() as testing_client:
        with client.app_context():
            yield testing_client
