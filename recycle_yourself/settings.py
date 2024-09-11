# from pathlib import Path
# import os



# LOGIN_REDIRECT_URL = '/profile/myProfile/'

# BASE_DIR = Path(__file__).resolve().parent.parent

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'main_app', 'static'),
# ]


# SECRET_KEY = '7+9e7sl#x2)nh^l$u-3b1b*s@$uk2%(!k0r8p=v7lcml(9b-i2'


# DEBUG = True

# ALLOWED_HOSTS = []


# # Application definition

# INSTALLED_APPS = [
#     'main_app',
#     'crispy_forms',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'recycle_yourself.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# CRISPY_TEMPLATE_PACK = 'bootstrap4'

# WSGI_APPLICATION = 'recycle_yourself.wsgi.application'



# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'kindnessconnect',
#          'USER': 'postgres',
#          'PASSWORD': 'postgres',
#          'HOST': 'localhost',  # or your PostgreSQL server's IP address
#          'PORT': '5432',  # default PostgreSQL port
#      }
#  }



# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]




# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True

# GOOGLE_MAPS_API_KEY = 'AIzaSyBa8r1tJ6u1356eClhlD2kkU503ooK5ZDs'


# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
# STATICFILES_DIRS = [
#      'C:\\kindnessconnect\\eden-lian\\main_app\\static',
# ]

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ALLOWED_HOSTS = ['kindnessconnect.westeurope.cloudapp.azure.com', '20.86.150.183']
                  
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Static files settings
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'main_app', 'static'),
# ]

# SECRET_KEY = '7+9e7sl#x2)nh^l$u-3b1b*s@$uk2%(!k0r8p=v7lcml(9b-i2'

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7+9e7sl#x2)nh^l$u-3b1b*s@$uk2%(!k0r8p=v7lcml(9b-i2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['kindnessconnect.westeurope.cloudapp.azure.com', '20.86.150.183']

# Application definition
INSTALLED_APPS = [
    'main_app',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recycle_yourself.urls'

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
                'django.template.context_processors.media',  # Add this line for media
            ],
        },
    },
]

WSGI_APPLICATION = 'recycle_yourself.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kindnessconnect',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main_app', 'static'),
]

# Media files (Uploads)
MEDIA_URL = '/post_pics/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'post_pics')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login redirect
LOGIN_REDIRECT_URL = '/profile/myProfile/'

# Google Maps API Key
GOOGLE_MAPS_API_KEY = 'AIzaSyBa8r1tJ6u1356eClhlD2kkU503ooK5ZDs'

# Debug ALLOWED_HOSTS
if DEBUG:
    ALLOWED_HOSTS += ['localhost', '127.0.0.1']
