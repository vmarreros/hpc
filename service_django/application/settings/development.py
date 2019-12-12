from .base import *

DEBUG = True

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# The age of session cookies, in seconds. (1 day)
SESSION_COOKIE_AGE = 86400

# Whether to expire the session when the user closes their browser.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# If this is set to True, the cookie will be marked as “secure”, which means browsers may ensure that
# the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Redirects all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = False
