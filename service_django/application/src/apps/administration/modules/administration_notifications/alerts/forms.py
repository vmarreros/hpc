from django import forms
from django.utils.translation import ugettext_lazy as _
import copy

from src.apps.notifications.models import Alert
from src.apps.security.models import LDAPUser, LDAPUserImported


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class AlertCreate(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['level', 'subject', 'message', 'to_ldap_user', 'to_ldap_imported_user']
        widgets = {
            'to_ldap_user': forms.CheckboxSelectMultiple,
            'to_ldap_imported_user': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        self.fields['level'].label = _('Alerta')
        self.fields['level'].widget.attrs['aria-describedby'] = 'level_icon'
        self.fields['level'].widget.attrs['icon'] = 'glyphicon glyphicon-bookmark'
        self.fields['level'].widget.attrs['class'] = 'form-control'
        self.fields['level'].choices = (("success", _("Éxito")), ("info", _("Información")), ("warning", _("Advertencia")), ("error", _("Error")))

        self.fields['subject'].label = _('Asunto')
        self.fields['subject'].widget.attrs['aria-describedby'] = 'subject_icon'
        self.fields['subject'].widget.attrs['icon'] = 'glyphicon glyphicon-globe'
        self.fields['subject'].widget.attrs['class'] = 'form-control'

        self.fields['message'].label = _('Mensaje')
        self.fields['message'].widget.attrs['aria-describedby'] = 'message_icon'
        self.fields['message'].widget.attrs['icon'] = 'glyphicon glyphicon-text'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = 3

        self.fields['to_ldap_user'].label = _('Usuarios ldap')

        self.fields['to_ldap_imported_user'].label = _('Usuarios ldap importados')

    def save(self, commit=True):
        instance = super(AlertCreate, self).save(commit=False)
        #
        if commit:
            # save to data base
            instance.from_user = self.request.security_user
            instance.save()
            self.save_m2m()
        return instance


class AlertDetail(forms.ModelForm):
    created = forms.DateField(
        label=_('HPC___SOFTWARE___REQUEST___LABEL___Requested'),
        required=False,
        widget=forms.DateInput(
            attrs={
                'aria-describedby': 'created_icon',
                'icon': 'glyphicon glyphicon-time',
            },
        ),
    )
    modified = forms.DateField(
        label=_('HPC___SOFTWARE___REQUEST___LABEL___Requested'),
        required=False,
        widget=forms.DateInput(
            attrs={
                'aria-describedby': 'modified_icon',
                'icon': 'glyphicon glyphicon-time',
            },
        ),
    )

    class Meta:
        model = Alert
        fields = ['level', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        self.fields['level'].label = _('Alerta')
        self.fields['level'].widget.attrs['aria-describedby'] = 'level_icon'
        self.fields['level'].widget.attrs['icon'] = 'glyphicon glyphicon-bookmark'

        self.fields['subject'].label = _('Asunto')
        self.fields['subject'].widget.attrs['aria-describedby'] = 'subject_icon'
        self.fields['subject'].widget.attrs['icon'] = 'glyphicon glyphicon-globe'

        self.fields['message'].label = _('Mensaje')
        self.fields['message'].widget.attrs['aria-describedby'] = 'message_icon'
        self.fields['message'].widget.attrs['icon'] = 'glyphicon glyphicon-globe'

        self.fields['created'].label = _('Creado')
        self.fields['created'].widget.attrs['aria-describedby'] = 'created_icon'
        self.fields['created'].widget.attrs['icon'] = 'glyphicon glyphicon-time'

        self.fields['modified'].label = _('Modificado')
        self.fields['modified'].widget.attrs['aria-describedby'] = 'modified_icon'
        self.fields['modified'].widget.attrs['icon'] = 'glyphicon glyphicon-time'


class AlertUpdate(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['level', 'subject', 'message', 'to_ldap_user', 'to_ldap_imported_user']
        widgets = {
            'to_ldap_user': forms.CheckboxSelectMultiple,
            'to_ldap_imported_user': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)

        self.fields['level'].label = _('Alerta')
        self.fields['level'].widget.attrs['aria-describedby'] = 'level_icon'
        self.fields['level'].widget.attrs['icon'] = 'glyphicon glyphicon-bookmark'
        self.fields['level'].widget.attrs['class'] = 'form-control'
        self.fields['level'].choices = (("success", _("Éxito")), ("info", _("Información")), ("warning", _("Advertencia")), ("error", _("Error")))

        self.fields['subject'].label = _('Asunto')
        self.fields['subject'].widget.attrs['aria-describedby'] = 'subject_icon'
        self.fields['subject'].widget.attrs['icon'] = 'glyphicon glyphicon-globe'
        self.fields['subject'].widget.attrs['class'] = 'form-control'

        self.fields['message'].label = _('Mensaje')
        self.fields['message'].widget.attrs['aria-describedby'] = 'message_icon'
        self.fields['message'].widget.attrs['icon'] = 'glyphicon glyphicon-text'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = 3

        self.fields['to_ldap_user'].label = _('Usuarios ldap')

        self.fields['to_ldap_imported_user'].label = _('Usuarios ldap importados')


class AlertDelete(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
