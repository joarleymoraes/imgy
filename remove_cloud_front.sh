#!/bin/bash

aws cloudformation  delete-stack --stack-name imgy-cf-api
aws cloudformation wait stack-delete-complete --stack-name imgy-cf-api