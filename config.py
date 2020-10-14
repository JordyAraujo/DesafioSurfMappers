import os


class Config(object):
    ALLOWED_EXTENSIONS = ["JPEG", "JPG", "PNG"]
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'galeriasm'
    AWS_ACCESS_KEY_ID = 'AKIA5VIHLDO3PDEYTTZP'
    AWS_SECRET_ACCESS_KEY = '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'
    BUCKET = 'galeriasmbucket'
    AWS_REGION_NAME = 'sa-east-1'}
