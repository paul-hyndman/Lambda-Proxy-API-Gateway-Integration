
from aws_cdk import (
    core,
    aws_sns as _sns,
    aws_sns_subscriptions as _subs,
    aws_dynamodb as _dynomodb,
    aws_logs as _logs,
    aws_lambda as _lambda,
    aws_apigateway as _apigw
)

class CustomLambdaStack(core.Stack):
    
    def __init__(self, scope: core.Construct, construct_id: str, table: _dynomodb.Table, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Read Lambda Code    
        with open("resource_stacks/lambda_src/lambda_processor.py", mode="r") as f:
            function_code = f.read()
                
        lambda_fn = _lambda.Function(
            self,
            "functionId",
            function_name="custom_lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            code=_lambda.InlineCode(
                function_code),
            timeout=core.Duration.seconds(10),
            environment={
                'LOG_LEVEL' : 'INFO',
                'table_name': table.table_name
            }
        )
        
        # Give function privileges to DynamoDb table
        table.grant_write_data(lambda_fn)
        
        # Create log group group.  Log group/logs removed when stack is destroyed
        log_group = _logs.LogGroup(
            self,
            "logGroupId",
            log_group_name=f"/aws/lambda/{lambda_fn.function_name}",
            removal_policy= core.RemovalPolicy.DESTROY
        )
        
        # Add API Gateway using REST API as Lambda front end.
        # Using Lambda API proxy, so Lambda must handle different HTTP methods
        api_gw_integration = _apigw.LambdaRestApi(
            self, 
            "lambda_fn_endpoint",
            handler=lambda_fn
        )
        
        output = core.CfnOutput(
            self,
            "API URL",
            value=f"{api_gw_integration.url}",
            description="browser-based URL for this Lamba fn"
        )