# imgy
Serverless Image Processing Service

## TL;DR


## Docs:

TODO

## Architecture

TODO

## Requirements

- An AWS Account
- Python 3.6

## CONFIGURE!

At `zappa_settings.py` you SHALL change:

- `profile_name`: which is AWS CLI profile we will use for deployed. Make sure it has ADMIN permission.
- `s3_bucket`: the S3 bucket where we will store our (zappa) deployment packages
- `imgy_bucket`: the S3 bucket from where we will get input images

You MAY also configure:

- `aws_region`: the AWS region to where you want to deploy the app
-  `imgy_cache_max_age`: Cache Control header max-age

## Deploy

`pip install zappa`
`deploy zappa api`

NOTE: you can also use virtualenv to install zappa.


## Undeploy
`undeploy zappa api`



# Sample Usage

`GET https://<host>/test.png?w=100&h=200`


# Available Transformations

All transformation below are independent of each other:

- `w`: sets image width
- `h`: sets image height
- `fm`: sets image format, e.g.: png, jpeg, etc. All supported by ImageMagick.
- `q`: sets compression quality, in case it's lossy format.







