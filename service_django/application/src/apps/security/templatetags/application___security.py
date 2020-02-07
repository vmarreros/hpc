from src.apps.security import models
from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags import staticfiles
from django.utils import timezone

register = template.Library()


@register.filter()
def get_string_title(request):
    return '-%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN,)


@register.filter()
def get_string_group_user(request):
    return '%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), request.security_user.identifier)


@register.filter()
def get_boolean_not(boolean):
    return not boolean


@register.filter()
def required_security_user(request):
    if request.security_user is not None:
        return True
    return False


@register.filter()
def security_user_has_permission(request, string___identifiers_to_verify):
    if required_security_user(request=request):
        set_identifier___to_verify = set(' '.join(string___identifiers_to_verify.split()).split())  # delete space
        if request.security_user.is_superuser is True or request.security_user.___boolean___has_permission___(set_identifier___to_verify=set_identifier___to_verify):
            return True
    return False


@register.filter()
def security_user_is_localuser(request):
    if required_security_user(request=request):
        if isinstance(request.security_user, models.LOCALUser):
            return True
    return False


@register.filter()
def security_user_is_ldapuser_or_ldapuserimported(request):
    if required_security_user(request=request):
        if isinstance(request.security_user, models.LDAPUser) or isinstance(request.security_user, models.LDAPUserImported):
            return True
    return False


@register.filter()
def security_user_is_ldapuser(request):
    if required_security_user(request=request):
        if isinstance(request.security_user, models.LDAPUser):
            return True
    return False


@register.filter()
def security_user_is_ldapuserimported(request):
    if required_security_user(request=request):
        if isinstance(request.security_user, models.LDAPUserImported):
            return True
    return False


@register.filter()
def get_instance_security_user(request):
    return request.security_user


@register.filter()
def get_string_security_user_url_current(request):
    return request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___']


@register.filter()
def get_string_security_user_avatar_url(request):
    string___avatar_url = staticfiles.static('apps/security/img/avatar/avatar.png')
    if request.security_user is not None and request.security_user.avatar:
        string___avatar_url = request.security_user.avatar.url
    return '%s?%s' % (string___avatar_url, timezone.datetime.now().strftime("%Y%m%d%H%M%S"))


@register.filter()
def get_string_notification_user_avatar_url(user):
    string___avatar_url = staticfiles.static('apps/security/img/avatar/avatar.png')
    if user.avatar:
        string___avatar_url = user.avatar.url
    return '%s?%s' % (string___avatar_url, timezone.datetime.now().strftime("%Y%m%d%H%M%S"))


@register.filter()
def get_string_security_user_ldap_group(request):
    if security_user_is_ldapuser_or_ldapuserimported(request=request):
        if security_user_is_ldapuser(request=request):
            return '%s_' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),)
        if security_user_is_ldapuserimported(request=request):
            return '%s_' % (request.security_user.ldap_group.lower(),)
    return ''


@register.filter()
def get_string_user_avatar_url(instance):
    string___avatar_url = staticfiles.static('apps/security/img/avatar/avatar.png')
    if instance is not None and instance.avatar:
        string___avatar_url = instance.avatar.url
    return '%s?%s' % (string___avatar_url, timezone.datetime.now().strftime("%Y%m%d%H%M%S"))


@register.filter()
def get_string_user_ldap_group(instance):
    if instance is None:
        return '%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN,)
    if isinstance(instance, models.LDAPUserRequest):
        return '%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN,)
    if isinstance(instance, models.LDAPUser):
        return '%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN,)
    if isinstance(instance, models.LDAPUserImported):
        return '%s' % (instance.ldap_group,)
    return ''


@register.filter()
def get_string_user_ldap_identifier(instance):
    if isinstance(instance, models.LDAPUserRequest):
        return '%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), instance.identifier, )
    if isinstance(instance, models.LDAPUser):
        return '%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), instance.identifier, )
    if isinstance(instance, models.LDAPUserImported):
        return '%s_%s' % (instance.ldap_group.lower(), instance.identifier, )
    return ''


@register.filter()
def get_string_user_th_width(request, string___identifiers_to_verify):
    if request.security_user is not None:
        list_identifier___to_verify = list(' '.join(string___identifiers_to_verify.split()).split())  # delete space
        if list_identifier___to_verify[0] != 'none':
            boolean___has_permission_0 = request.security_user.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[0], })
        else:
            boolean___has_permission_0 = False
        if list_identifier___to_verify[1] != 'none':
            boolean___has_permission_1 = request.security_user.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[1], })
        else:
            boolean___has_permission_1 = False
        if list_identifier___to_verify[2] != 'none':
            boolean___has_permission_2 = request.security_user.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[2], })
        else:
            boolean___has_permission_2 = False
        if list_identifier___to_verify[3] != 'none':
            boolean___has_permission_3 = request.security_user.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[3], })
        else:
            boolean___has_permission_3 = False
        #
        if boolean___has_permission_1 and boolean___has_permission_2 and boolean___has_permission_3:
            return 'th___width_3'
        if (boolean___has_permission_1 and boolean___has_permission_2) or (boolean___has_permission_1 and boolean___has_permission_3) or (boolean___has_permission_2 and boolean___has_permission_3):
            return 'th___width_2'
        if boolean___has_permission_1 or boolean___has_permission_2 or boolean___has_permission_3:
            return 'th___width_1'
        if boolean___has_permission_0:
            return 'th___width_1'
    return 'th___width_0'


@register.filter()
def get_boolean_show_the_administration_link(request):
    if required_security_user(request=request):
        if request.security_user.is_superuser is True:
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_localuser_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_localuserrequest_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_ldapuser_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_ldapuserrequest_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_ldapuserimported_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_group_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_security_permission_list', }):
            return True
        if request.security_user.___boolean___has_permission___(set_identifier___to_verify={'application_help_document_list', }):
            return True
    return False
