from . import forms
from src.apps.notifications import models

# The model to administrate
___MODEL___ = models.Alert
# The model path to administrate
___MODEL_PATH___ = 'alerts'
# The forms of the model to administrate
___FORM___CREATE___ = forms.AlertCreate
___FORM___DETAIL___ = forms.AlertDetail
___FORM___UPDATE___ = forms.AlertUpdate
___FORM___DELETE___ = forms.AlertDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 1000000
