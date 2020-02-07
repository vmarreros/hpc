from django import http
from django.contrib import messages

from src.apps.security import decorators, utils as utils_security
from src.apps.hpc import utils
from src.apps.hpc import models
from .forms import SoftwareRequestForm


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def installed(request):
    dict___data = dict()
    softwares = models.SoftwareInstalled.objects.all()
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context={
            'softwares': softwares
        },
        template_name='apps/hpc/___includes___/content/center/hpc_software/installed.html'
    )
    return http.JsonResponse(dict___data)


def request_software(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    form = SoftwareRequestForm(data=request.POST or None, request=request)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account = request.security_user.group_identifier()
            instance.save()
            messages.add_message(request, messages.SUCCESS, "La solicitud a sido enviada a los administradores.")
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___MODAL___'] = utils.___html___template_modal___message___(request=request)
        else:
            messages.add_message(request, messages.ERROR, "El formulario contiene errores.")
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
            dict___data['___HTML___MODAL___'] = utils.___html___template___(
                request=request,
                context={
                    'form': form
                },
                template_name='apps/hpc/___includes___/modal/hpc/request_software.html'
            )
        dict___data['___HTML___MODAL___MESSAGE___'] = utils.___html___template_message___(request=request)
    else:
        dict___data['___HTML___MODAL___'] = utils.___html___template___(
            request=request,
            context={
                'form': form
            },
            template_name='apps/hpc/___includes___/modal/hpc/request_software.html'
        )
    return http.JsonResponse(dict___data)
