from django.urls import path, include

app_name = 'administration'

urlpatterns = [
    path('localuser/', include(('src.apps.administration.modules.administration_security.localuser.urls', app_name), namespace='localuser')),
    path('localuserrequest/', include(('src.apps.administration.modules.administration_security.localuserrequest.urls', app_name), namespace='localuserrequest')),
    path('ldapuser/', include(('src.apps.administration.modules.administration_security.ldapuser.urls', app_name), namespace='ldapuser')),
    path('ldapuserrequest/', include(('src.apps.administration.modules.administration_security.ldapuserrequest.urls', app_name), namespace='ldapuserrequest')),
    path('ldapuserimported/', include(('src.apps.administration.modules.administration_security.ldapuserimported.urls', app_name), namespace='ldapuserimported')),
    path('group/', include(('src.apps.administration.modules.administration_security.group.urls', app_name), namespace='group')),
    path('permission/', include(('src.apps.administration.modules.administration_security.permission.urls', app_name), namespace='permission')),
]
