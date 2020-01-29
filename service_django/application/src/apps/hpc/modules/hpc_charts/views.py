# -*- coding: utf-8 -*-

# django modules import
from django.http import HttpResponse, JsonResponse

# user modules import
from src.apps.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from src.apps.hpc import utils as utils___hpc
from ...slurm import Command, CommandError


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def nodes(request):
    dict___data = dict()
    command = Command(
        request,
        'nodes')
    try:
        data = command.to_dict()
    except CommandError as e:
        return utils___hpc.___httpresponse___error___(request)
    dict___data['___HTML___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
        request=request,
        context={'data': data},
        template_name='apps/hpc/___includes___/content/center/hpc_charts/nodes.html'
    )
    return JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def nodes_json(request):
    command = Command(
        request,
        'nodes')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils___hpc.___httpresponse___error___(request)
    return HttpResponse(data, content_type='application/json')


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def jobs(request):
    command = Command(request, 'jobs')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils___hpc.___httpresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def users(request):
    command = Command(request, 'report users')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils___hpc.___httpresponse___error___(request)
