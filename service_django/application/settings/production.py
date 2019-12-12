from .base import *

DEBUG = False

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env_variable('DJANGO_EMAIL_HOST')
EMAIL_PORT = get_env_variable('DJANGO_EMAIL_PORT')
EMAIL_USER_NOREPLY = get_env_variable('DJANGO_EMAIL_USER_NOREPLY')

# The age of session cookies, in seconds. (1 day)
SESSION_COOKIE_AGE = 86400

# Whether to expire the session when the user closes their browser.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# If this is set to True, the cookie will be marked as “secure”, which means browsers may ensure that
# the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Redirects all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = True
