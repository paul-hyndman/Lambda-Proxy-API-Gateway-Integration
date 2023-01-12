#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from resource_stacks.custom_lambda import CustomLambdaStack
from resource_stacks.dynamodb import DynamoDBStack

app = cdk.App()
# vpc_stack = CustomVpcStack(app, "CustomVpcStack")
# CustomEc2Stack(app, "CustomEc2Stack", vpc=vpc_stack.vpc)
dynamoDBStack = DynamoDBStack(app, "DynamoDBStackapp")
CustomLambdaStack(app, "CustomLambdaStack", dynamoDBStack.table)
app.synth()
