# imgy
Serverless Image Processing Service

### TL;DR


### Docs:

TODO

### Architecture

![Architecture](https://raw.githubusercontent.com/joarleymoraes/imgy/master/docs/architecture.png)

### Requirements

- An AWS Account
- Python 3.6

### CONFIGURE!

At `zappa_settings.py` you SHALL change:

- `profile_name`: which is the AWS CLI profile we will use for deployment. Make sure it has ADMIN permission.
- `s3_bucket`: the S3 bucket where we will store our (zappa) deployment packages. You don't need to create in AWS, Zappa will do it for you.

You MAY also configure:
- `aws_region`: the AWS region to where you want to deploy the app


At `imgy/settings.py` you SHALL change:
- `imgy_bucket`: the S3 bucket from where we will get input images.


You MAY also configure:
-  `imgy_cache_max_age`: Define the cache Control header max-age in seconds.

### Deploy

- `pip install zappa`
- `deploy zappa api`

NOTE: you can also use `virtualenv` to install zappa.


### Undeploy
`undeploy zappa api`


# Demo

[https://vk05slewjg.execute-api.us-west-2.amazonaws.com/api/cloud.png?w=100&h=100&fm=jpg&q=50](https://vk05slewjg.execute-api.us-west-2.amazonaws.com/api/cloud.png?w=100&h=100&fm=jpg&q=50)


# Available Transformations

All transformationS below are independent of each other:

- `w`: sets image width
- `h`: sets image height
- `fm`: sets image format, e.g.: png, jpeg, etc. All supported by ImageMagick.
- `q`: sets compression quality, in case it's lossy format. Value must be between 1 to 100.


