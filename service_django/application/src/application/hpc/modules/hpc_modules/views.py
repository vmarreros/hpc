# -*- coding: utf-8 -*-
# django modules import
from django import http
from django.views.decorators.csrf import csrf_exempt

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from ... import utils as utils___hpc
from ... import models


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def index(request):
    dict___data = dict()
    modules = models.Module.objects.all()
    dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
        request=request,
        context={
            'modules': modules
        },
        template_name='application/hpc/___includes___/content/center/hpc_modules/index.html'
    )
    return http.JsonResponse(dict___data)
