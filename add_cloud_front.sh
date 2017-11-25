#!/bin/bash

if [ -z "$1" ]; then
  echo "ERROR: Missing <api_id>."
  exit
fi

API_ID=$2

aws cloudformation deploy --stack-name imgy-cf-api --template-body file://cf_add_cloud_front.json --parameters ApiId=${API_ID}