# Django settings for ua_67 project.
import os
import cloudinary
import dj_database_url

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH,'templates')
STATIC_PATH = os.path.join(PROJECT_PATH,'static')
DATABASE_PATH = os.path.join(PROJECT_PATH,'Union_1.db')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMINS = (
    ('Sylvestre Gug', 'sgug@outlook.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',     # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DATABASE_PATH,                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if os.getenv('DATABASE_URL'):
    DEBUG = False
    TEMPLATE_DEBUG = False

    # Update database configuration with $DATABASE_URL.
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = os.environ['SECRET_KEY']

    #############################
    #
    # CLOUDINARY CONFIG
    #
    #############################
    cloudinary.config (
        cloud_name = os.environ['CLOUDINARY_NAME'],
        api_key = os.environ['CLOUDINARY_API_KEY'],
        api_secret = os.environ['CLOUDINARY_API_SECRET']
    )

    #############################
    #
    # MEMCACHE CONFIG
    #
    #############################

    os.environ['MEMCACHE_SERVERS']  = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
    os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

    CACHES = {
        'default': {
            # Use pylibmc
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

            # Use binary memcache protocol (needed for authentication)
            'BINARY': True,

            # TIMEOUT is not the connection timeout! It's the default expiration
            # timeout that should be applied to keys! Setting it to `None`
            # disables expiration.
            'TIMEOUT': None,

            'OPTIONS': {
                # Enable faster IO
                'no_block': True,
                'tcp_nodelay': True,

                # Keep connection alive
                'tcp_keepalive': True,

                # Timeout for set/get requests
                '_poll_timeout': 2000,

                # Use consistent hashing for failover
                'ketama': True,

                # Configure failover timings
                'connect_timeout': 2000,
                'remove_failed': 4,
                'retry_timeout': 2,
                'dead_timeout': 10
            }
        }
    }

    FLICKR_API_KEY = os.environ['FLICKR_API_KEY']
    FLICKR_SECRET =  os.environ['FLICKR_SECRET']
    FLICKR_USERID =  os.environ['FLICKR_USERID']


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')
#MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    STATIC_PATH,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ua_67.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ua_67.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'Union_1',
    'cloudinary',
    'flickr_gallery',
)

#CLOUDINARY_URL='cloudinary://594761675313837:ARNma0lZjgYBaK9VPWGxSRF6xCo@deiq0pyek'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

if os.getenv('POSTMARK_API_TOKEN'):
    EMAIL_BACKEND =         'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST =            'smtp.postmarkapp.com'
    EMAIL_HOST_PASSWORD =   os.environ['POSTMARK_API_TOKEN']
    EMAIL_HOST_USER =       os.environ['POSTMARK_API_TOKEN']
    EMAIL_PORT =            '587'
    EMAIL_USE_TLS =         True
    SERVER_EMAIL =          os.environ['POSTMARK_INBOUND_ADDRESS']

    POSTMARK_API_KEY     =  os.environ['POSTMARK_API_KEY']
    POSTMARK_SENDER      = 'union@alsace.nyc'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

try:
    from local_settings import *
except:
    pass