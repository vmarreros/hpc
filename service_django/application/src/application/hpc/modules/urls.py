# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'hpc'

urlpatterns = [
    path('hpc_jobs/', include(('src.application.hpc.modules.hpc_jobs.urls', app_name), namespace='hpc_jobs')),
    path('hpc_script/', include(('src.application.hpc.modules.hpc_script.urls', app_name), namespace='hpc_script')),
    path('hpc_nodes/', include(('src.application.hpc.modules.hpc_nodes.urls', app_name), namespace='hpc_nodes')),
    path('hpc_explorer/', include(('src.application.hpc.modules.hpc_explorer.urls', app_name), namespace='hpc_explorer')),
    path('hpc_software/', include(('src.application.hpc.modules.hpc_software.urls', app_name), namespace='hpc_software')),
    path('hpc_charts/', include(('src.application.hpc.modules.hpc_charts.urls', app_name), namespace='hpc_charts')),
]
