import json
from unittest.mock import patch

import pytest

from functions.device.app_get import lambda_handler


@pytest.fixture
def mock_lambda_adapter_exception():
    with patch('functions.device.lambda_adapter.LambdaAdapter.handle_request', side_effect=Exception("Test error")) as mock:
        yield mock


def test_lambda_handler_exception(mock_lambda_adapter_exception):
    event = {"headers": {"OAuth-Token": "invalid_token"}}
    context = {}

    response = lambda_handler(event, context)

    assert response['statusCode'] == 400
    # 确保响应体包含错误信息
    assert "Test error" in json.loads(response['body'])["message"]
    mock_lambda_adapter_exception.assert_called_once_with(event)
