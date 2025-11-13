import pytest
from api_client import YougileAPI


@pytest.fixture(scope="session")
def api():
    return YougileAPI()


@pytest.fixture
def new_project(api):
    
    response = api.create_project("Test Project")
    assert response.status_code == 200, f"Project not created: {response.text}"
    project = response.json()
    yield project  