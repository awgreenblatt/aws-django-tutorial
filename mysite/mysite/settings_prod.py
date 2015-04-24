from settings_common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_STORAGE = 'mysite.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE= 'mysite.MediaRootS3BotoStorage'

AWS_ACCESS_KEY_ID = 'your-access-key-here'
AWS_SECRET_ACCESS_KEY = 'your-secret-key-here'

AWS_STORAGE_BUCKET_NAME = 'django-meetup'
STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

