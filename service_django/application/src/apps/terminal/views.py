from django.shortcuts import render

from src.apps.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)


@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def init(request):
    return render(request, 'apps/terminal/application_terminal.html')
