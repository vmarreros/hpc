from django import http
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import os

from src.apps.security import decorators, utils as utils_security
from src.apps.hpc import utils
from src.apps.hpc import ssh, linux
from src.apps.hpc.slurm import CommandError
from . import forms
from . import script


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def index(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == "POST":
        instance = request.security_user
        form = forms.ScriptForm(data=request.POST, request=request)
        if form.is_valid():
            script_name = form.cleaned_data.get('script_name') + '.sl'
            file = os.path.join(settings.MEDIA_ROOT, script_name + str(timezone.now()))
            with open(file, 'wb') as f:
                for line in script.build(form).splitlines():
                    f.write(bytes(line, 'utf-8') + b'\n')
            boolean_error = ssh.ssh_sftp_put(instance.group_identifier(), instance.private_key.path, file, '/home/CLUSTER/%s/%s' % (instance.group_identifier(), script_name))
            os.unlink(file)
            if boolean_error:
                messages.add_message(request, messages.ERROR, _('HPC___SSH___MESSAGES_ScriptSendErr'))
            else:
                form = forms.ScriptForm(request=request)
                if request.POST.get('run'):
                    result = ssh.ssh_exec(instance.group_identifier(), instance.private_key.path, 'sbatch "' + script_name + '"')
                    if result[0]:
                        messages.add_message(request, messages.WARNING, _('HPC___SSH___MESSAGES_ScriptReleasedErr') % result[1].decode('utf-8'))
                    else:
                        messages.add_message(request, messages.SUCCESS, _('HPC___SSH___MESSAGES_ScriptReleasedOk') % result[1].decode('utf-8'))
                else:
                    messages.add_message(request, messages.SUCCESS, _('HPC___SSH___MESSAGES_ScriptSendOk'))
            dict___data['___HTML___MODAL___'] = utils.___html___template_modal___message___(request=request)
            dict___data['___HTML___MODAL___MESSAGE___'] = utils.___html___template_message___(request=request)
            dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
                request=request,
                context={
                    'form': form,
                },
                template_name='apps/hpc/___includes___/content/center/hpc_script/index.html'
            )
            return http.JsonResponse(dict___data)
        else:
            messages.add_message(request, messages.ERROR, _('HPC___SSH___MESSAGES_ScriptFormErr'))
            dict___data['___BOOLEAN___ERROR___'] = True
            dict___data['___HTML___MODAL___'] = utils.___html___template_modal___message___(request=request)
            dict___data['___HTML___MODAL___MESSAGE___'] = utils.___html___template_message___(request=request)
            dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
                request=request,
                context={
                    'form': form
                },
                template_name='apps/hpc/___includes___/content/center/hpc_script/index.html'
            )
            return http.JsonResponse(dict___data)
    else:
        try:
            form = forms.ScriptForm(request=request)
        except CommandError:
            return utils.___httpresponse___error___(request)
        dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
            request=request,
            context={
                'form': form,
                'method': 'GET'},
            template_name='apps/hpc/___includes___/content/center/hpc_script/index.html'
        )
        return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def vars(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    data = linux.generate_data_dict(request, option='envVars')
    if data:
        dict___data['___HTML___MODAL___'] = utils.___html___template___(
            request=request,
            context={
                'variables': data
            },
            template_name='apps/hpc/___includes___/modal/hpc/variables.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils.___jsonresponse___error___(request)
