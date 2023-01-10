from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SK')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
  'dentist-site-1.sentey.repl.co',
  'd3cc99ee-8b25-4042-8bd1-49689a111528.id.repl.co', 'localhost', '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = [
  'https://dentist-site-1.sentey.repl.co',
  'https://d3cc99ee-8b25-4042-8bd1-49689a111528.id.repl.co',
]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_METHODS = [
  "DELETE",
  "GET",
  "OPTIONS",
  "PATCH",
  "POST",
  "PUT",
]

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'cloudinary_storage',
  'cloudinary',
  'core',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  "whitenoise.middleware.WhiteNoiseMiddleware",
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# CLOUDINARY_STORAGE = {
#   'CLOUD_NAME': os.getenv('CN'),
#   'API_KEY': os.getenv('AK'),
#   'API_SECRET': os.getenv('AS')
# }
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# STATIC_URL = '/dentist/static/'
# STATIC_ROOT = BASE_DIR / 'dentist/static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'testingouteqw@outlook.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')
EMAIL_USE_TLS = True

X_FRAME_OPTIONS = '*'
