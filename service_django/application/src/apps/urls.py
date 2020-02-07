from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog

from . import views

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('hpc',),
}

urlpatterns = [
    path('', view=views.index, name='application'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('captcha/', include('captcha.urls')),
    path('website/', include('src.apps.website.urls', namespace='website')),
    path('hpc/', include('src.apps.hpc.urls', namespace='hpc')),
    path('bigdata/', include('src.apps.bigdata.urls', namespace='bigdata')),
    path('terminal/', include('src.apps.terminal.urls', namespace='terminal')),
    path('administration/', include('src.apps.administration.urls', namespace='administration')),
    path('help/', include('src.apps.help.urls', namespace='help')),
    path('notifications/', include('src.apps.notifications.urls', namespace='notifications')),
    path('secret/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
