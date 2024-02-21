import os
import jsonschema
import yaml
from functions.device.i_device_port import IRequestParamValidatePort


class RequestParamValidateAdapter(IRequestParamValidatePort):
    def validate(self, event):
        # 构造DeviceFetchParam对象
        param = {
            "user_id": event['pathParameters']['user_id'],
            "Authorization": event['headers'].get('Authorization', ''),
            "X-BOC-Owner-Id": int(event['headers'].get('X-BOC-Owner-Id', 0)),
            "Service-Program": event['headers'].get('Service-Program', '')
        }

        # 加载JSON Schema进行验证
        current_dir = os.path.dirname(os.path.abspath(__file__))
        schema_file = os.path.join(current_dir, "../schemas/param.yml")

        with open(schema_file, "r", encoding="utf-8") as fp:
            param_schema = yaml.safe_load(fp)
            jsonschema.validate(instance=param, schema=param_schema)
