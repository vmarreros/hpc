# -*- coding: utf-8 -*-
# django modules import
from django import http
from django.contrib import messages

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from src.application.hpc import utils as utils___hpc
from ... import models
from .forms import SoftwareRequestForm


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def installed(request):
    dict___data = dict()
    softwares = models.SoftwareInstalled.objects.all()
    dict___data['___HTML___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
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
            instance.account = request.___APPLICATION___SECURITY___USER___.group_identifier()
            instance.save()
            messages.add_message(request, messages.SUCCESS, "La solicitud a sido enviada a los administradores.")
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template_modal___message___(request=request)
        else:
            messages.add_message(request, messages.ERROR, "El formulario contiene errores.")
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
            dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
                request=request,
                context={
                    'form': form
                },
                template_name='apps/hpc/___includes___/modal/hpc/request_software.html'
            )
        dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
    else:
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': form
            },
            template_name='apps/hpc/___includes___/modal/hpc/request_software.html'
        )
    return http.JsonResponse(dict___data)
