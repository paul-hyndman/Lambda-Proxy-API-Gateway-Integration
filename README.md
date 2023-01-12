# Project highlights how, using CDK, the following:
#   - Create Lambda Proxy Integration in API Gateway
#   - Create Lambda and Dynamo AWS infrastructure using Python and CDK
#   - Expose an public REST API for the Lambda
#   - Python Lambda function puts message to a Dynamo Database


# When deployed, issue a POST to example URL (start of URL path will vary):
#    https://wb77wjto32.execute-api.us-east-1.amazonaws.com/prod/
#    POST payload like:
#      {
#          "orderId" : "9",
#          "customerId" : "999",
#          "sku" : "110-rrgt555",
#          "quantity" : 5
#      }

Requirements:
 - A command shell such as Git Bash
 - Python
 - CDK
 - Node JS/NPM for miscellaneous package installs
 - Postman or CURL to test API

This is a modification of an earlier project which deployed a Java REST API instead of a Lambda Gateway Proxy Integration
See https://github.com/paul-hyndman/DynamoDB-with-Java-REST-APIs for more info
