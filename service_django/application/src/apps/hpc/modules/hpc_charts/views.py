from django.http import HttpResponse, JsonResponse

from src.apps.security import decorators, utils as utils_security
from src.apps.hpc import utils
from src.apps.hpc.slurm import Command, CommandError


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def nodes(request):
    dict___data = dict()
    command = Command(
        request,
        'nodes')
    try:
        data = command.to_dict()
    except CommandError as e:
        return utils.___httpresponse___error___(request)
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context={'data': data},
        template_name='apps/hpc/___includes___/content/center/hpc_charts/nodes.html'
    )
    return JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def nodes_json(request):
    command = Command(
        request,
        'nodes')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils.___httpresponse___error___(request)
    return HttpResponse(data, content_type='application/json')


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def jobs(request):
    command = Command(request, 'jobs')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils.___httpresponse___error___(request)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def users(request):
    command = Command(request, 'report users')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils.___httpresponse___error___(request)
