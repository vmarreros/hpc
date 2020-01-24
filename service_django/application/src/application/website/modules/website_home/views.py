# -*- coding: utf-8 -*-
from ... import utils as utils___website
from src.application.home import models
from src.application.security import (
    decorators as decorators___application___security,
)
from django import http


@decorators___application___security.___required___request_is_ajax___()
def index(request):
    dict___data = dict()
    instance = models.Document.objects.all().filter(is_active=True).reverse().first()
    context = dict()
    if instance is not None:
        context.update({
            'ctx___instance': instance,
            'ctx___title': instance,
            'ctx___content': instance.___string___content___(),
        })
    dict___data['___HTML___WEBSITE___CONTENT___CENTER___'] = utils___website.___html___template___(
        request=request,
        context=context,
        template_name='apps/website/___includes___/content/center/website_home/index.html',
    )
    return http.JsonResponse(dict___data)
