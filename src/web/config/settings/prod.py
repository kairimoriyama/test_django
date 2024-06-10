from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # False
ALLOWED_HOSTS = list(env("ALLOWED_HOSTS"))



# where collectstatic will collect static files for deployment
STATIC_ROOT = '/usr/share/nginx/html/static' #ボリュームマウント先のパス
# user-uploaded files.
MEDIA_ROOT = '/usr/share/nginx/html/media' #ボリュームマウント先のパス

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST':"db", #コンテナのサーバ名
        'PORT': 5432,
    }
}


# HTTPS設定後
CSRF_COOKIE_SECURE = True # Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True # Set this to True to avoid transmitting the session cookie over HTTP accidentally.



# 以下、ログ設定

# ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # stylistdivision アプリケーションが利用するロガー
        'stylistdivision': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    # ハンドラの設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',  # ログローテーション(新しいファイルへの切り替え)間隔の単位(D=日)
            'interval': 3,  # ログローテーション間隔(3日単位)
            'backupCount': 7,  # 保存しておくログファイル数
        },
    },

    # フォーマッタの設定
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
