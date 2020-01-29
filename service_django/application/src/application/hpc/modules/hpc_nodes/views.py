# -*- coding: utf-8 -*-
import random

# django modules import
from django import http

# user modules import
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from src.application.hpc import utils as utils___hpc
from ...slurm import Command, CommandError


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def index(request):
    dict___data = dict()
    command = Command(request, 'nodes')
    try:
        data = command.to_dict()
    except CommandError as e:
        return utils___hpc.___httpresponse___error___(request)
    data.update({'random': random.random()})
    dict___data['___HTML___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
        request=request,
        context=data,
        template_name='apps/hpc/___includes___/content/center/hpc_nodes/index.html'
    )
    return http.JsonResponse(dict___data)
