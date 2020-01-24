# -*- coding: utf-8 -*-
from . import forms
from src.application.hpc import models

# The model to administrate
___MODEL___ = models.SoftwareRequested
# The model path to administrate
___MODEL_PATH___ = 'requested'
# The forms of the model to administrate
___FORM___DETAIL___ = forms.SoftwareRequestedDetail
___FORM___UPDATE___ = forms.SoftwareRequestedUpdate
___FORM___DELETE___ = forms.SoftwareRequestedDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 1000000
