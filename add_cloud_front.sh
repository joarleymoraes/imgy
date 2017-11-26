#!/bin/bash

if [ -z "$1" ]; then
  echo "ERROR: Missing <api_id>."
  exit
fi

API_ID=$1

aws cloudformation create-stack --stack-name imgy-cf-api --template-body file://cf_add_cloud_front.json --parameters ParameterKey=ApiId,ParameterValue=${API_ID}
aws cloudformation wait stack-create-complete --stack-name imgy-cf-api
aws cloudformation describe-stacks --stack-name imgy-cf-api