import pytest
from jsonschema import ValidationError

from functions.device.request_param_validate_adapter import RequestParamValidateAdapter

valid_event = {
    "headers": {
        "OAuth-Token": "a" * 16,
        "Authorization": "valid_authorization",
        "X-BOC-Owner-Id": "1",
        "Service-Program": "brother_plus_us"
    }
}

missing_param_event = {
    "headers": {}
}

invalid_param_event = {
    "headers": {
        "OAuth-Token": "short",
        "Authorization": "",
        "X-BOC-Owner-Id": "0",
        "Service-Program": "invalid_program"
    }
}

@pytest.fixture
def validator():
    return RequestParamValidateAdapter()

def test_missing_params(validator):
    with pytest.raises(ValidationError):
        validator.validate(missing_param_event)

def test_invalid_params(validator):
    with pytest.raises(ValidationError):
        validator.validate(invalid_param_event)

def test_valid_params(validator):
    validator.validate(valid_event)

