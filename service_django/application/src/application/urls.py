from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import javascript_catalog

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('hpc',),
}

urlpatterns = [
    url(regex=r'^$', view=views.index, name='application'),
    url(r'^jsi18n/(?P<packages>\S+?)/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^website/', include('src.application.website.urls', namespace='website')),
    url(r'^hpc/', include('src.application.hpc.urls', namespace='hpc')),
    url(r'^bigdata/', include('src.application.bigdata.urls', namespace='bigdata')),
    url(r'^administration/', include('src.application.administration.urls', namespace='administration')),
    url(r'^secret/', admin.site.urls),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
