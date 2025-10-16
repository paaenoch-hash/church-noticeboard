import os
import dj_database_url

from pathlib import Path
from datetime import timedelta

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings


SECRET_KEY = os.environ.get('@2^zbd%vyp*!uem7n20hn^d7((50$kmuyp*jju)9z*#y!c0l%l', 'dev-secret-key')
DEBUG = os.getenv('DEBUG', 'True') == 'False'
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://church_noticeboard.onrender.com']

# Installed apps for Django, REST Framework, CORS, and Channels
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'channels',
    'notice',
    'whitenoise.runserver_nostatic',
    
]

ROOT_URLCONF = 'noticeboard.urls'


# Middleware for CORS and standard Django functionality
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings for frontend communication
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    "http://127.0.0.1:5173",
    'https://ttagnoticeboard.info',
    'https://noticeboard-ui.vercel.app',  # Update after Vercel deployment
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False
# REST Framework settings for JWT authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# ASGI application for WebSocket support
ASGI_APPLICATION = 'noticeboard.asgi.application'

# Channels configuration with Redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1'))],
        },
    },
}

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3')}

# Static and media file settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'





# JWT settings for authentication
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}