from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','localhost']


# user-uploaded files.
MEDIA_ROOT = [BASE_DIR/"media"] 

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ATOMIC_REQUESTS': True, # BEGIN, COMMITの発行が1回だけ
    }
}