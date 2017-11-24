import io
import os
import ntpath
import tempfile
import magic
from flask import Flask, send_file, request, abort
# from flask_cors import CORS
from wand.image import Image
from imgy.settings import AWS_REGION, BUCKET, CACHE_MAX_AGE, LOSSY_IMAGE_FMTS, DEFAULT_QUALITY_RATE
from imgy.s3_helper import S3Helper

app = Flask(__name__)
# Adding CORS support
# CORS(app)

s3 = S3Helper(AWS_REGION)

def is_lossy(ext, ops):
    return ('fm' in ops and ops['fm'] in LOSSY_IMAGE_FMTS) or ext in LOSSY_IMAGE_FMTS

def get_mime_type(file_path):
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)

#
# Adding cache_control header to every response
# So that transformed images can be cached at CloudFront
#
@app.after_request
def add_header(response):
    if response.status_code == 200:
        response.cache_control.max_age = CACHE_MAX_AGE
    return response


def image_transform(filename, ops):
    """
    Transform the image specified by `filename` using the transformations specified by `ops` (operations)
    Returns
    -------
    str
        the filename of the transformed image
    """
    basename = ntpath.basename(filename)
    name, ext = os.path.splitext(basename)
    ext = ext.strip('.')

    code, path = tempfile.mkstemp()
    output = path + '.' + ext

    with Image(filename=filename) as src:
        with src.clone() as img:
            #
            # handling resizing
            #
            if 'w' in ops and 'h' in ops:
                w, h = int(ops['w']), int(ops['h']),
                img.resize(w, h)
            elif 'w' in ops:
                w, h = int(ops['w']), img.height,
                img.resize(w, h)
            elif 'h' in ops:
                w, h = img.width, int(ops['h']),
                img.resize(w, h)

            #
            # handling format conversion
            #
            if 'fm' in ops:
                ext = ops['fm']
                img.format = ext
            
            #
            # handling quality compression for lossy images
            #
            if is_lossy(ext, ops):
                if 'q' in ops:
                    q = int(ops['q'])
                else:
                    q = DEFAULT_QUALITY_RATE

                img.compression_quality = 99

            img.save(filename=output)


    return output


@app.route('/<s3_key>', methods=['GET'])
def transform(s3_key):
    #
    # getting query string as dict
    #
    ops = request.args.to_dict()

    print(ops)

    img_filename = s3.download(BUCKET, s3_key)

    if img_filename:
        output_img = image_transform(img_filename, ops)
    else:
        abort(404)

    #
    # Thanks for the magic:
    # https://blog.zappa.io/posts/serving-binary-data-through-aws-api-gateway-automatically-with-zappa
    #
    with open(output_img, 'rb') as fp:
        mime_type = get_mime_type(output_img)
        return send_file(
                    io.BytesIO(fp.read()),
                    attachment_filename=output_img,
                    mimetype='image/jpg'
               )


if __name__ == '__main__':
    app.run(debug=True)