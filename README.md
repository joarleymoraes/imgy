# imgy
Serverless Image Processing Service

### TL;DR

![Demo](https://raw.githubusercontent.com/joarleymoraes/imgy/master/docs/demo.gif)

### Docs:

TODO

### Architecture

![Architecture](https://raw.githubusercontent.com/joarleymoraes/imgy/master/docs/architecture.png)

### Requirements

- An AWS Account
- Python 3.6
- virtualenv
- AWS CLI

### CONFIGURE!

At `zappa_settings.py` you SHALL change:

- `s3_bucket`: the S3 bucket where we will store our (zappa) deployment packages. You don't need to create in AWS, Zappa will do it for you.

NOTE: make sure the default AWS CLI profile has ADMIN permission.

You MAY also configure:
- `aws_region`: the AWS region to where you want to deploy the app


At `imgy/settings.py` you SHALL change:
- `imgy_bucket`: the S3 bucket from where we will get input images.


You MAY also configure:
-  `imgy_cache_max_age`: Define the cache Control header max-age in seconds.

### Deploy

- `virtualenv -p python3.6 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `deploy zappa`

### Adding CloudFront (optional)

You may add a custom CloudFront distribution, which will add an effective caching layer to your service. Be aware that this step will take about 15-20 minutes to finish. At the end the CloudFront URL will be generated, use this instead of the API Gateways'.

`./add_cloud_front.sh`


### Undeploy
`undeploy zappa`


# Demo

[https://vk05slewjg.execute-api.us-west-2.amazonaws.com/api/cloud.png?w=100&h=100&fm=jpg&q=50](https://vk05slewjg.execute-api.us-west-2.amazonaws.com/api/cloud.png?w=100&h=100&fm=jpg&q=50)

CloudFront URL:




# Available Transformations

All transformationS below are independent of each other:

- `w`: sets image width
- `h`: sets image height
- `fm`: sets image format, e.g.: png, jpeg, etc. All supported by ImageMagick.
- `q`: sets compression quality, in case it's lossy format. Value must be between 1 to 100.


