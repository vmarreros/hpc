from django import http

import random

from src.apps.security import decorators, utils as utils_security
from src.apps.hpc import utils
from src.apps.hpc.slurm import Command, CommandError


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def index(request):
    dict___data = dict()
    command = Command(request, 'nodes')
    try:
        data = command.to_dict()
    except CommandError as e:
        return utils.___httpresponse___error___(request)
    data.update({'random': random.random()})
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context=data,
        template_name='apps/hpc/___includes___/content/center/hpc_nodes/index.html'
    )
    return http.JsonResponse(dict___data)
