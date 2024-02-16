from app.adapters.lambda_adapter import LambdaAdapter


def lambda_handler(event, context):
    lambda_adapter = LambdaAdapter()
    return lambda_adapter.handle(event, context)
