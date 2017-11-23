import json
import os

json_data = open('zappa_settings.json')
zappa_settings = json.load(json_data)['api']

AWS_REGION = zappa_settings['aws_region']

BUCKET = zappa_settings['imgy_bucket']

CACHE_MAX_AGE = zappa_settings['imgy_cache_max_age']

DEFAULT_QUALITY_RATE = 80

LOSSY_IMAGE_FMTS = ('jpg', 'jpeg', 'webp')



