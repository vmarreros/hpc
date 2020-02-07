from django import http, shortcuts

from src.apps.security import decorators, utils as utils_security
from src.apps.bigdata import utils
from src.apps.notifications.models import Alert


@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index(request):
    dict___context = dict()
    return shortcuts.render(
        request=request,
        context=dict___context,
        template_name='apps/bigdata/application___bigdata.html'
    )


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index___load(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___LOAD___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/bigdata/___includes___/load/load.html'
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index___title(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___TITLE___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/bigdata/___includes___/title/title.html'
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index___header(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___HEADER___'] = utils.___html___template___(
        request=request,
        context={
            'alerts': Alert.objects.get_alerts_unread_by_user(request)
        },
        template_name='apps/bigdata/___includes___/header/header.html'
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index___leftside(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___LEFTSIDE___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/bigdata/___includes___/leftside/leftside.html'
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index___content___center(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/bigdata/___includes___/content/center/index.html'
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def index___content___footer(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___CONTENT___FOOTER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='apps/bigdata/___includes___/content/footer/footer.html'
    )
    return http.JsonResponse(dict___data)


@decorators.ajax_required()
def login(request):
    return utils_security.___jsonresponse___login___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators.ajax_required()
def login___forgot_credentials_1(request):
    return utils_security.___jsonresponse___login___forgot_credentials_1___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators.ajax_required()
def login___forgot_credentials_2(request, pk):
    return utils_security.___jsonresponse___login___forgot_credentials_2___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___,
        pk=pk
    )


@decorators.ajax_required()
def login___forgot_credentials_3(request, pk):
    return utils_security.___jsonresponse___login___forgot_credentials_3___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___,
        pk=pk
    )


@decorators.ajax_required()
def login___request(request):
    return utils_security.___jsonresponse___login___request___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def logout(request):
    return utils_security.___jsonresponse___logout___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators.ajax_required()
@decorators.security_user_is_ldapuser_or_ldapuserimported(___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def profile(request):
    return utils_security.___jsonresponse___profile___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators.ajax_required()
def locale(request):
    return utils_security.___jsonresponse___locale___(
        request=request,
        ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )
