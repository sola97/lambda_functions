import pytest
from jsonschema import ValidationError

from functions.device.request_param_validate_adapter import RequestParamValidateAdapter

# 测试数据准备
valid_event = {
    "headers": {
        "OAuth-Token": "a" * 16,  # 16个字符长的字符串
        "Authorization": "valid_authorization",
        "X-BOC-Owner-Id": "1",  # 确保这是一个有效的ID
        "Service-Program": "brother_plus_us"
    }
}

missing_param_event = {
    "headers": {}
}

invalid_param_event = {
    "headers": {
        "OAuth-Token": "short",  # 太短
        "Authorization": "",  # 空字符串
        "X-BOC-Owner-Id": "0",  # 无效的ID
        "Service-Program": "invalid_program"  # 无效的枚举值
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
    # 应该不抛出异常
    validator.validate(valid_event)

