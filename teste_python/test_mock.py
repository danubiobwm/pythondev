import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    # Create a mock object
    mock = MagicMock()

    # Set up the mock to return a specific value when called
    mock.status_code = 200
    mock.json.return_value = {"key": "value"}
    return mock

def test_api_response(mock_response):
    # Use the mock object in your test
    assert mock_response.status_code == 200
    assert mock_response.json() == {"key": "value"}