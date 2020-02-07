from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import date, timedelta

from src.apps.security import decorators, utils as utils_security
from src.apps.hpc import utils
from src.apps.hpc.slurm import Command, CommandError


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def history(request):
    dict___data = dict()
    today = date.today()
    day = today - timedelta(days=7)
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context={
            'date': day.strftime("%Y-%m-%d")},
        template_name='apps/hpc/___includes___/content/center/hpc_jobs/history.html'
    )
    return JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def history_json(request):
    command = Command(
        request,
        'history',
        request.GET.get('date', None))
    try:
        data = command.to_json()
    except CommandError as e:
        return utils.___httpresponse___error___(request)
    return HttpResponse(data, content_type='application/json')


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def queue(request):
    dict___data = dict()
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context={},
        template_name='apps/hpc/___includes___/content/center/hpc_jobs/queue.html'
    )
    return JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def queue_json(request):
    command = Command(
        request,
        'jobs')
    try:
        data = command.to_json()
    except CommandError as e:
        return utils.___httpresponse___error___(request)
    return HttpResponse(data, content_type='application/json')


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def detail_job(request):
    dict___data = dict()
    command = Command(
        request,
        'job-detail',
        request.GET.get('jobid', None))
    data = command.to_dict()
    try:
        pass
    except CommandError as e:
        return utils.___httpresponse___error___(request)
    dict___data['detail'] = utils.___html___template___(
        request=request,
        context={'data': data},
        template_name='apps/hpc/___includes___/content/center/hpc_jobs/detail_job.html'
    )
    return JsonResponse(dict___data)


@csrf_exempt
@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def action_job(request):
    if request.method == 'POST':
        dict___data = dict()
        command = Command(
            request,
            request.POST.get('option', None),
            request.POST.get('jobID', None))
        command.to_dict()
        command = Command(
            request,
            'job-detail',
            request.POST.get('jobID', None))
        data = command.to_dict()
        dict___data['detail'] = utils.___html___template___(
            request=request,
            context={
                'data': data
            },
            template_name='apps/hpc/___includes___/content/center/hpc_jobs/detail_job.html'
        )
        return JsonResponse(dict___data)
    return utils.___httpresponse___error___(request)
