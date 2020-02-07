from django import http
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from src.apps.security import decorators
from src.apps.help import utils as utils
from src.apps.help import models


@decorators.ajax_required()
def index(request):
    dict___data = dict()
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/help/___includes___/content/center/help_document/index.html',
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
def list(request):
    dict___data = dict()
    instances = models.Document.objects.all().filter(is_active=True)
    dict___data['___HTML___CONTENT___CENTER___LIST___'] = utils.___html___template___(
        request=request,
        context={
            'ctx___instances': instances,
        },
        template_name='apps/help/___includes___/content/center/help_document/___includes___/list.html',
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
def content(request, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return utils.___jsonresponse___error___(request=request)
    if pk != 0:
        instance = models.Document.objects.___instance___by_pk___(pk=pk)
        if instance is None:
            messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
            return utils.___jsonresponse___error___(request=request)
        dict___data['___HTML___CONTENT___CENTER___CONTENT___'] = utils.___html___template___(
            request=request,
            context={
                'ctx___title': instance,
                'ctx___content': instance.___string___content___(),
            },
            template_name='apps/help/___includes___/content/center/help_document/___includes___/content.html',
        )
    else:
        instances = models.Document.objects.all().filter(is_active=True)
        if instances.count() > 0:
            instance = instances[0]
            dict___data['___HTML___CONTENT___CENTER___CONTENT___'] = utils.___html___template___(
                request=request,
                context={
                    'ctx___title': instance,
                    'ctx___content': instance.___string___content___(),
                },
                template_name='apps/help/___includes___/content/center/help_document/___includes___/content.html',
            )
        else:
            dict___data['___HTML___CONTENT___CENTER___CONTENT___'] = utils.___html___template___(
                request=request,
                context=dict(),
                template_name='apps/help/___includes___/content/center/help_document/___includes___/content.html',
            )

    return http.JsonResponse(dict___data)
