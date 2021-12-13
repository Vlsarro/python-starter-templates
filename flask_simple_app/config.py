import os


SITE_HOST = os.environ.get('flask_site_host') or '0.0.0.0'
PORT = os.environ.get('flask_site_port') or 5000
DEBUG = False
ENCODING = 'utf-8'
ROOT_PATH = os.path.dirname(__file__)

TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')
STATIC_PATH = os.path.join(ROOT_PATH, 'static')
UPLOAD_PATH = os.path.join(ROOT_PATH, 'uploads')

USE_SSL = False

# Local certificate generation
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
# USE_SSL_CERT = True
USE_SSL_CERT = False

env_secret_key = os.environ.get('flask_secret_key')
if env_secret_key:
    SECRET_KEY = env_secret_key.encode(ENCODING)
else:
    SECRET_KEY = b'not_really_a_secret'
