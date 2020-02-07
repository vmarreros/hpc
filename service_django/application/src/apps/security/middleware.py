from . import models, utils
from django.utils import translation


class ApplicationSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        instance = None
        if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') and (request.session.get('___APPLICATION___SECURITY___USER___PK___')):
            if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') == utils.security_user_localuser:
                instance = models.LOCALUser.objects.___instance___by_pk___(pk=request.session.get('___APPLICATION___SECURITY___USER___PK___'))
            if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') == utils.security_user_ldapuser:
                instance = models.LDAPUser.objects.___instance___by_pk___(pk=request.session.get('___APPLICATION___SECURITY___USER___PK___'))
            if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') == utils.security_user_ldapuserimported:
                instance = models.LDAPUserImported.objects.___instance___by_pk___(pk=request.session.get('___APPLICATION___SECURITY___USER___PK___'))
            if instance is not None:
                translation.activate(instance.locale)
                request.session[translation.LANGUAGE_SESSION_KEY] = instance.locale
        request.security_user = instance
        #
        list_string___url = (
            '/website/',
            '/website/modules/website_home/',
            '/hpc/',
            '/hpc/modules/hpc_jobs/history/',
            '/hpc/modules/hpc_jobs/queue/',
            '/hpc/modules/hpc_script/',
            '/hpc/modules/hpc_nodes/',
            '/hpc/modules/hpc_explorer/',
            '/hpc/modules/hpc_software/installed/',
            '/bigdata/',
            '/bigdata/modules/bigdata_module01/',
            '/administration/',
            '/administration/modules/administration_security/localuser/',
            '/administration/modules/administration_security/localuserrequest/',
            '/administration/modules/administration_security/ldapuser/',
            '/administration/modules/administration_security/ldapuserrequest/',
            '/administration/modules/administration_security/ldapuserimported/',
            '/administration/modules/administration_security/group/',
            '/administration/modules/administration_security/permission/',
            '/administration/modules/administration_help/document/',
            '/help/',
            '/help/modules/help_document/',
            '/notifications/',
        )
        if request.path in list_string___url:
            if request.path == '/website/':
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = '/website/modules/website_home/'
            elif request.path == '/hpc/':
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = '/hpc/modules/hpc_jobs/queue/'
            elif request.path == '/bigdata/':
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = '/bigdata/modules/bigdata_module01/'
            else:
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = request.path

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
