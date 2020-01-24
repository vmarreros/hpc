# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from src.application.hpc.models import SoftwareRequested


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


class SoftwareRequestForm(forms.ModelForm):
    class Meta:
        model = SoftwareRequested
        fields = ['software', 'website', 'version', 'type', 'installation_guide', 'motivation']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        ___field___attribute___placeholder___locale___reload__(field=self.fields['software'], locale='HPC___SOFTWARE___REQUEST___PLACEHOLDER___Name')
        self.fields['software'].widget.attrs['autofocus'] = True
        self.fields['software'].widget.attrs['class'] = 'form-control'
        self.fields['software'].widget.attrs['aria-describedby'] = 'software_icon'
        self.fields['software'].widget.attrs['icon'] = 'glyphicon glyphicon-globe'

        ___field___attribute___placeholder___locale___reload__(field=self.fields['website'], locale='HPC___SOFTWARE___REQUEST___PLACEHOLDER___Website')
        self.fields['website'].widget.attrs['class'] = 'form-control'
        self.fields['website'].widget.attrs['aria-describedby'] = 'website_icon'
        self.fields['website'].widget.attrs['icon'] = 'glyphicon glyphicon-link'

        ___field___attribute___placeholder___locale___reload__(field=self.fields['version'], locale='HPC___SOFTWARE___REQUEST___PLACEHOLDER___Version')
        self.fields['version'].widget.attrs['class'] = 'form-control'
        self.fields['version'].widget.attrs['aria-describedby'] = 'version_icon'
        self.fields['version'].widget.attrs['icon'] = 'glyphicon glyphicon-tag'

        ___field___attribute___placeholder___locale___reload__(field=self.fields['type'], locale='HPC___SOFTWARE___REQUEST___PLACEHOLDER___Type')
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['aria-describedby'] = 'type_icon'
        self.fields['type'].widget.attrs['icon'] = 'glyphicon glyphicon-th-list'

        ___field___attribute___placeholder___locale___reload__(field=self.fields['installation_guide'], locale='HPC___SOFTWARE___REQUEST___PLACEHOLDER___Installation_guide')
        self.fields['installation_guide'].widget.attrs['class'] = 'form-control'
        self.fields['installation_guide'].widget.attrs['aria-describedby'] = 'installation_guide_icon'
        self.fields['installation_guide'].widget.attrs['icon'] = 'glyphicon glyphicon-link'

        ___field___attribute___placeholder___locale___reload__(field=self.fields['motivation'], locale='HPC___SOFTWARE___REQUEST___PLACEHOLDER___Motivation')
        self.fields['motivation'].widget.attrs['class'] = 'form-control'
        self.fields['motivation'].widget.attrs['aria-describedby'] = 'motivation_icon'
        self.fields['motivation'].widget.attrs['icon'] = 'glyphicon glyphicon-question-sign'
        self.fields['motivation'].widget.attrs['rows'] = 3
