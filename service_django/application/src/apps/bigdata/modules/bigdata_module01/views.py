from django import http

from src.apps.security import decorators, utils as utils_security
from src.apps.bigdata import utils


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index(request):
    dict___data = dict()
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/bigdata/___includes___/content/center/bigdata_module01/index.html'
    )
    return http.JsonResponse(dict___data)
