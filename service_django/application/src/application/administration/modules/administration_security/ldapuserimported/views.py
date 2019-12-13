# -*- coding: utf-8 -*-
from .... import utils as utils___application___administration
from .. import utils as utils___application___administration___module
from . import utils as utils___application___administration___module___model
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)


@decorators___application___security.___required___request_is_ajax___()
def index(request):
    return utils___application___administration.___jsonresponse___index___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___has_permission___(
    ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_ldapuserimported_list', }
)
def list(request):
    return utils___application___administration.___jsonresponse___list___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___has_permission___(
    ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_ldapuserimported_list', 'application_security_ldapuserimported_detail', }
)
def detail(request, pk):
    return utils___application___administration.___jsonresponse___detail___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model,
        pk=pk
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___has_permission___(
    ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_ldapuserimported_list', 'application_security_ldapuserimported_update', }
)
def update(request, pk):
    return utils___application___administration.___jsonresponse___update___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model,
        pk=pk
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___has_permission___(
    ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___,
    set_identifier___to_verify={'application_security_ldapuserimported_list', 'application_security_ldapuserimported_delete', }
)
def delete(request, pk):
    return utils___application___administration.___jsonresponse___delete___(
        request=request,
        ___utils___module___=utils___application___administration___module,
        ___utils___module_model___=utils___application___administration___module___model,
        pk=pk
    )
