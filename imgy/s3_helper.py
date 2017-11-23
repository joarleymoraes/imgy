import boto3
from boto3.exceptions import ResourceNotExistsError
from botocore.exceptions import ClientError
import logging
import os
import ntpath
import tempfile

logger = logging.getLogger(__name__)


def get_resource(res_name, region, aws_key=None, aws_secret=None):
    try:
        return boto3.resource(res_name, region, aws_access_key_id=aws_key,
                                aws_secret_access_key=aws_secret)
    except ResourceNotExistsError:
        pass


class S3Helper(object):
    def __init__(self, region, aws_key=None, aws_secret=None):
        self.region = region
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        self.resource = get_resource('s3', self.region, aws_key=self.aws_key,
                                     aws_secret=self.aws_secret)


    def download(self, bucket, key):
        """
        Download the file from s3 given `bucket` and `key`.
        Returns
        -------
        str
            the filename of the downloaded file or None if the file was not found
        """
        f_info = bucket + ':' + key
        basename = ntpath.basename(key)
        name, ext = os.path.splitext(basename)
        logger.info('Downloading file from s3 at {}'.format(f_info))
        code, tmp_file = tempfile.mkstemp()
        tmp_file = tmp_file + '.' + ext
        try:
            self.resource.Bucket(bucket).download_file(key, tmp_file)
        except ClientError:
            logger.exception('File not found: {}'.format(f_info))
        else:
            return tmp_file


    