import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-1234567890')  # Change for production
DEBUG = os.getenv('DEBUG', 'True') == 'False'
ALLOWED_HOSTS = ['*']

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

    'https://your-frontend.vercel.app',  # Update after Vercel deployment
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

# Database configuration (SQLite for local dev, update for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static and media file settings
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'





# JWT settings for authentication
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}