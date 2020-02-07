from src.apps.security import decorators, utils as utils_security
from src.apps.administration import utils
from .. import utils as utils___application___administration___module
from . import utils as utils___application___administration___module___model


@decorators.ajax_required()
def index(request):
    return utils.___jsonresponse___index___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model
    )


@decorators.ajax_required()
@decorators.security_user_has_permission(
    ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_localuser_list', }
)
def list(request):
    return utils.___jsonresponse___list___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model
    )


@decorators.ajax_required()
@decorators.security_user_has_permission(
    ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_localuser_list', 'application_security_localuser_create', }
)
def create(request):
    return utils.___jsonresponse___create___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model
    )


@decorators.ajax_required()
@decorators.security_user_has_permission(
    ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_localuser_list', 'application_security_localuser_detail', }
)
def detail(request, pk):
    return utils.___jsonresponse___detail___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model,
        pk=pk
    )


@decorators.ajax_required()
@decorators.security_user_has_permission(
    ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_localuser_list', 'application_security_localuser_update', }
)
def update(request, pk):
    return utils.___jsonresponse___update___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model,
        pk=pk
    )


@decorators.ajax_required()
@decorators.security_user_has_permission(
    ___application___security___from___module___=utils_security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_localuser_list', 'application_security_localuser_delete', }
)
def delete(request, pk):
    return utils.___jsonresponse___delete___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model,
        pk=pk
    )
