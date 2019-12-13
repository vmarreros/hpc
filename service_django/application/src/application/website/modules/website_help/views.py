# -*- coding: utf-8 -*-
from ... import utils as utils___website
from src.application.help import models
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security,
)
from django import http
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


@decorators___application___security.___required___request_is_ajax___()
def index(request):
    dict___data = dict()
    dict___data['___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___'] = utils___website.___html___template___(
        request=request,
        context=dict(),
        template_name='application/website/___includes___/content/center/website_help/index.html',
    )
    return http.JsonResponse(dict___data)


def list(request):
    dict___data = dict()
    instances = models.Document.objects.all().filter(is_active=True)
    dict___data['___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___LIST___'] = utils___website.___html___template___(
        request=request,
        context={
            'ctx___instances': instances,
        },
        template_name='application/website/___includes___/content/center/website_help/___includes___/list.html',
    )
    return http.JsonResponse(dict___data)


def content(request, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return utils___website.___jsonresponse___error___(request=request)
    if pk != 0:
        instance = models.Document.objects.___instance___by_pk___(pk=pk)
        if instance is None:
            messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
            return utils___website.___jsonresponse___error___(request=request)
        dict___data['___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___CONTENT___'] = utils___website.___html___template___(
            request=request,
            context={
                'ctx___title': instance,
                'ctx___content': instance.___string___content___(),
            },
            template_name='application/website/___includes___/content/center/website_help/___includes___/content.html',
        )
    else:
        instances = models.Document.objects.all().filter(is_active=True)
        if instances.count() > 0:
            instance = instances[0]
            dict___data['___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___CONTENT___'] = utils___website.___html___template___(
                request=request,
                context={
                    'ctx___title': instance,
                    'ctx___content': instance.___string___content___(),
                },
                template_name='application/website/___includes___/content/center/website_help/___includes___/content.html',
            )
        else:
            dict___data['___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___CONTENT___'] = utils___website.___html___template___(
                request=request,
                context=dict(),
                template_name='application/website/___includes___/content/center/website_help/___includes___/content.html',
            )

    return http.JsonResponse(dict___data)
