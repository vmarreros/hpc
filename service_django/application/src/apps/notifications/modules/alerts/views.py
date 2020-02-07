from django import http

from src.apps.security import decorators, utils as utils_security
from src.apps.notifications import utils
from src.apps.notifications.models import Alert


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def detail(request, pk):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    alert = Alert.objects.get(pk=pk)
    if alert:
        dict___data['___HTML___MODAL___'] = utils.___html___template___(
            request=request,
            context={
                'alert': alert
            },
            template_name='apps/notifications/___includes___/modal/alerts/detail.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils.___jsonresponse___error___(request)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def unread(request, pk):
    if request.method == "POST":
        dict___data = dict()
        dict___data['___BOOLEAN___ERROR___'] = False
        alert = Alert.objects.get(pk=pk)
        alert.unread = not alert.unread
        alert.save()
        return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def delete(request, pk):
    if request.method == "POST":
        dict___data = dict()
        dict___data['___BOOLEAN___ERROR___'] = False
        alert = Alert.objects.get(pk=pk)
        # alert.delete()
        return http.JsonResponse(dict___data)
