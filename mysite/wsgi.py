"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
import boto3

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
from io import StringIO, BytesIO

client_s3 = boto3.client(
    's3',
    region_name=os.environ.get('AWS_REGION', 'ap-northeast-1')
)

response = client_s3.get_object(
    Bucket=os.environ.get('DEPLOY_ENV_BUCKET'),
    Key=os.environ.get('DEPLOY_ENV_KEY')
)

load_dotenv(stream=StringIO(response.get("Body").read().decode("utf-8")), override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
