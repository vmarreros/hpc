from os import environ
from os.path import abspath, dirname, join
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


def root(*dirs):
    base_dir = join(dirname(__file__), '..')
    return abspath(join(base_dir, *dirs))


BASE_DIR = root()

DJANGO_CONFIGURATION = get_env_variable('ENVIRONMENT')

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'wsgi.application'

ROOT_URLCONF = 'src.application.urls'

# Installed applications
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'django_celery_beat',
    'django.contrib.auth',
    'django.contrib.admin',
    'admin_honeypot',
    'captcha',
    'src.application.security',
    'src.application.help',
    'src.application.home',
    'src.application.website',
    'src.application.statistic',
    'src.application.hpc',
    'src.application.bigdata',
    'src.application.administration',
]

# Middleware
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'src.application.security.middleware.ApplicationSecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Havana'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# List of languages used
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

# Directory that will host po and mo files
LOCALE_PATHS = (
    root('i18n/application/security/locale/application___security/locale'),
    #
    root('i18n/application/website/locale/application___website/locale'),
    root('i18n/application/website/locale/application___website___header/locale'),
    root('i18n/application/website/locale/application___website___leftside/locale'),
    root('i18n/application/website/locale/application___website___content/locale'),
    root('i18n/application/website/locale/application___website___content___website_home/locale'),
    root('i18n/application/website/locale/application___website___content___website_help/locale'),
    #
    root('i18n/application/hpc/locale/application___hpc/locale'),
    root('i18n/application/hpc/locale/application___hpc___header/locale'),
    root('i18n/application/hpc/locale/application___hpc___leftside/locale'),
    root('i18n/application/hpc/locale/application___hpc___content/locale'),
    root('i18n/application/hpc/locale/application___hpc___content___hpc_jobs/locale'),
    root('i18n/application/hpc/locale/application___hpc___content___hpc_script/locale'),
    root('i18n/application/hpc/locale/application___hpc___content___hpc_nodes/locale'),
    root('i18n/application/hpc/locale/application___hpc___content___hpc_explorer/locale'),
    root('i18n/application/hpc/locale/application___hpc___content___hpc_modules/locale'),
    root('i18n/application/hpc/locale/application___hpc___ssh/locale'),
    #
    root('i18n/application/bigdata/locale/application___bigdata/locale'),
    root('i18n/application/bigdata/locale/application___bigdata___header/locale'),
    root('i18n/application/bigdata/locale/application___bigdata___leftside/locale'),
    root('i18n/application/bigdata/locale/application___bigdata___content/locale'),
    root('i18n/application/bigdata/locale/application___bigdata___content___bigdata_module01/locale'),
    root('i18n/application/bigdata/locale/application___bigdata___content___bigdata_module02/locale'),
    root('i18n/application/bigdata/locale/application___bigdata___content___bigdata_module03/locale'),
    #
    root('i18n/application/administration/locale/application___administration/locale'),
    root('i18n/application/administration/locale/application___administration___header/locale'),
    root('i18n/application/administration/locale/application___administration___leftside/locale'),
    root('i18n/application/administration/locale/application___administration___content/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___localuser/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___localuserrequest/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___ldapuser/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___ldapuserrequest/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___ldapuserimported/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___group/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_security___permission/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_help___document/locale'),
    root('i18n/application/administration/locale/application___administration___content___admin_home___document/locale'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('POSTGRES_DB'),
        'USER': get_env_variable('POSTGRES_USER'),
        'PASSWORD': get_env_variable('POSTGRES_PASSWORD'),
        'HOST': get_env_variable('POSTGRES_HOST'),
        'PORT': get_env_variable('POSTGRES_PORT'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    root('staticfiles'),
)
STATIC_ROOT = join(dirname(BASE_DIR), 'volumes', 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = join(dirname(BASE_DIR), 'volumes', 'mediafiles')


# LDAP settings
LDAP_SERVER_HOST = get_env_variable('DJANGO_LDAP_SERVER_HOST')
LDAP_SERVER_PORT = int(get_env_variable('DJANGO_LDAP_SERVER_PORT'))
LDAP_SERVER_USER = get_env_variable('DJANGO_LDAP_SERVER_USER')
LDAP_SERVER_PASSWORD = get_env_variable('DJANGO_LDAP_SERVER_PASSWORD')[1:-1]
LDAP_SERVER_GROUPS_SEARCH_BASE = get_env_variable('DJANGO_LDAP_SERVER_GROUPS_SEARCH_BASE')
LDAP_SERVER_GROUPS_LIST = get_env_variable('DJANGO_LDAP_SERVER_GROUPS_LIST')[1:-1].split()
LDAP_SERVER_GROUPS_GROUP_CN = get_env_variable('DJANGO_LDAP_SERVER_GROUPS_GROUP_CN')
LDAP_SERVER_GROUPS_GROUP_GIDNUMBER = get_env_variable('DJANGO_LDAP_SERVER_GROUPS_GROUP_GIDNUMBER')
LDAP_SERVER_USERS_SEARCH_BASE = get_env_variable('DJANGO_LDAP_SERVER_USERS_SEARCH_BASE')
LDAP_SERVER_USERS_HPC_SEARCH_BASE = get_env_variable('DJANGO_LDAP_SERVER_USERS_HPC_SEARCH_BASE')
LDAP_SERVER_USERS_HOMEDIRECTORY = get_env_variable('DJANGO_LDAP_SERVER_USERS_HOMEDIRECTORY')

# CLUSTER settings
CLUSTER_SERVER_HOST = get_env_variable('DJANGO_CLUSTER_SERVER_HOST')
CLUSTER_SERVER_PORT = get_env_variable('DJANGO_CLUSTER_SERVER_PORT')

# Celery settings
CELERY_BROKER_URL = 'amqp://%s:%s@%s:%s//' % (
    get_env_variable('RABBITMQ_DEFAULT_USER'),
    get_env_variable('RABBITMQ_DEFAULT_PASS'),
    get_env_variable('RABBITMQ_HOST'),
    get_env_variable('RABBITMQ_PORT'),)
CELERY_RESULT_BACKEND = 'django-db'
