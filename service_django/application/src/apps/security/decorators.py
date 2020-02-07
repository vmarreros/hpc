from . import ldap, models, utils
from django import http, shortcuts
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


def jsonresponse_not_permission(request, ___application___security___from___module___):
    if request.is_ajax():
        dict___data = dict()
        dict___data['___BOOLEAN___ERROR___'] = True
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE Action not performed, you do not have permission.'))
        dict_string___application___security___from___module = utils.___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
        string___modal = dict_string___application___security___from___module['string___modal']
        string___modal___message = dict_string___application___security___from___module['string___modal___message']
        string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
        string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
        dict___data[string___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data['___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___'] = True
        dict___data['___APPLICATION___SECURITY___USER___URL_REDIRECT___'] = reverse(utils.security_user_url_reverse)
        return http.JsonResponse(dict___data)
    else:
        return shortcuts.redirect(reverse(utils.security_user_url_reverse))


def ajax_required(function=None):
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            if request.is_ajax():
                return view_func(request, *args, **kwargs)
            return shortcuts.redirect(reverse(utils.security_user_url_reverse))

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def required_security_user(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            if request.security_user is not None:
                return view_func(request, *args, **kwargs)
            return jsonresponse_not_permission(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def security_user_has_permission(function=None, ___application___security___from___module___='', set_identifier___to_verify=set()):
    def _decorator(view_func):
        @required_security_user(___application___security___from___module___=___application___security___from___module___)
        def _view(request, *args, **kwargs):
            if request.security_user.is_superuser is True or request.security_user.___boolean___has_permission___(set_identifier___to_verify=set_identifier___to_verify):
                return view_func(request, *args, **kwargs)
            return jsonresponse_not_permission(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def security_user_is_localuser(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @required_security_user()
        def _view(request, *args, **kwargs):
            if isinstance(request.security_user, models.LOCALUser):
                return view_func(request, *args, **kwargs)
            return jsonresponse_not_permission(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def security_user_is_ldapuser_or_ldapuserimported(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @required_security_user()
        def _view(request, *args, **kwargs):
            if isinstance(request.security_user, models.LDAPUser) or isinstance(request.security_user, models.LDAPUserImported):
                return view_func(request, *args, **kwargs)
            return jsonresponse_not_permission(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def security_user_is_ldapuser(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @required_security_user()
        def _view(request, *args, **kwargs):
            if isinstance(request.security_user, models.LDAPUser):
                return view_func(request, *args, **kwargs)
            return jsonresponse_not_permission(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def security_user_is_ldapuserimported(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @required_security_user()
        def _view(request, *args, **kwargs):
            if isinstance(request.security_user, models.LDAPUserImported):
                return view_func(request, *args, **kwargs)
            return jsonresponse_not_permission(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def required_ldap_connection(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            boolean___is_there_connection = False
            connection = ldap.___connection___ldap___()
            try:
                # start the connection
                if connection.bind():
                    boolean___is_there_connection = True
            except (Exception,):
                pass
            finally:
                # close the connection
                connection.unbind()
            if boolean___is_there_connection is False:
                dict___data = dict()
                dict___data['___BOOLEAN___ERROR___'] = True
                messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE Action not performed, connection to the LDAP could not be established.'))
                dict_string___application___security___from___module = utils.___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
                string___modal = dict_string___application___security___from___module['string___modal']
                string___modal___message = dict_string___application___security___from___module['string___modal___message']
                string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
                string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
                dict___data[string___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                dict___data[string___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                dict___data[string___modal___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                dict___data[string___modal___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                return http.JsonResponse(dict___data)
            else:
                return view_func(request, *args, **kwargs)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)
