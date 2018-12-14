# -*- coding: utf-8 -*-
from src.application.home import models
from django import forms
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import copy
import os
import shutil

___FIELD___IS_ACTIVE___ = forms.BooleanField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___IS_ACTIVE'),
    required=False,
    widget=forms.CheckboxInput(
        attrs={
            'id': 'is_active',
            'aria-describedby': 'is_active_icon',
            'icon': 'glyphicon glyphicon-check',
        },
    ),
)
___FIELD___CREATED___ = forms.DateField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___CREATED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'created',
            'aria-describedby': 'created_icon',
            'icon': 'glyphicon glyphicon-time',
        },
    ),
)
___FIELD___MODIFIED___ = forms.DateField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___MODIFIED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'modified',
            'aria-describedby': 'modified_icon',
            'icon': 'glyphicon glyphicon-time',
        },
    ),
)
___FIELD___TITLE___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___TITLE'),
    required=False,
    min_length=1,
    max_length=1024,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'title',
            'class': 'form-control',
            'aria-describedby': 'title_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___CONTENT___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___CONTENT'),
    required=False,
    widget=forms.Textarea(
        attrs={
            'id': 'content',
            'class': 'form-control',
            'rows': 5,
        },
    ),
)
___FIELD___IMAGE___ = forms.ImageField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___IMAGE'),
    required=False,
    widget=forms.FileInput(
        attrs={
            'id': 'image',
            'icon': 'glyphicon glyphicon-picture',
            'button_upload_id': 'image___button_upload_id',
            'img_upload_id': 'image___img_upload_id',
            'style': 'display: none;',
        },
    ),
)


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.home_text = '\"%s\"' % (_(locale),)


class DocumentCreate(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    title_en = copy.deepcopy(___FIELD___TITLE___)
    title_es = copy.deepcopy(___FIELD___TITLE___)
    content_en = copy.deepcopy(___FIELD___CONTENT___)
    content_es = copy.deepcopy(___FIELD___CONTENT___)
    image = ___FIELD___IMAGE___

    class Meta:
        model = models.Document
        fields = ['is_active', 'title_en', 'title_es', 'content_en', 'content_es', 'image', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # is_active
        ___field___attribute___help_text___locale___reload__(field=self.fields['is_active'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___IS_ACTIVE___HOME_TEXT')
        self.fields['is_active'].initial = True
        # title_en
        ___field___attribute___placeholder___locale___reload__(field=self.fields['title_en'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___TITLE')
        self.fields['title_en'].widget.attrs['id'] = 'title_en'
        self.fields['title_en'].widget.attrs['aria-describedby'] = 'title_en_icon'
        # title_es
        ___field___attribute___placeholder___locale___reload__(field=self.fields['title_es'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___TITLE')
        self.fields['title_es'].widget.attrs['id'] = 'title_es'
        self.fields['title_es'].widget.attrs['aria-describedby'] = 'title_es_icon'
        # content_en
        ___field___attribute___placeholder___locale___reload__(field=self.fields['content_en'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___CONTENT')
        self.fields['content_en'].widget.attrs['id'] = 'content_en'
        # content_es
        ___field___attribute___placeholder___locale___reload__(field=self.fields['content_es'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___CONTENT')
        self.fields['content_es'].widget.attrs['id'] = 'content_es'

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if self.files.get('image'):
            if len(self.files.get('image')) > 2 * 1024 * 1024:  # 2MB
                raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___IMAGE___VALIDATION The image should not be beggear than %(weight)s.') % {'weight': '2mb', })
        return image


class DocumentDetail(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    created = ___FIELD___CREATED___
    modified = ___FIELD___MODIFIED___
    title = ___FIELD___TITLE___
    content = ___FIELD___CONTENT___
    image = ___FIELD___IMAGE___

    class Meta:
        model = models.Document
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)


class DocumentUpdate(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    title_en = copy.deepcopy(___FIELD___TITLE___)
    title_es = copy.deepcopy(___FIELD___TITLE___)
    content_en = copy.deepcopy(___FIELD___CONTENT___)
    content_es = copy.deepcopy(___FIELD___CONTENT___)
    image = ___FIELD___IMAGE___

    class Meta:
        model = models.Document
        fields = ['is_active', 'title_en', 'title_es', 'content_en', 'content_es', 'image', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        # is_active
        ___field___attribute___help_text___locale___reload__(field=self.fields['is_active'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___IS_ACTIVE___HOME_TEXT')
        # title_en
        ___field___attribute___placeholder___locale___reload__(field=self.fields['title_en'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___TITLE')
        self.fields['title_en'].widget.attrs['id'] = 'title_en'
        self.fields['title_en'].widget.attrs['aria-describedby'] = 'title_en_icon'
        # title_es
        ___field___attribute___placeholder___locale___reload__(field=self.fields['title_es'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___TITLE')
        self.fields['title_es'].widget.attrs['id'] = 'title_es'
        self.fields['title_es'].widget.attrs['aria-describedby'] = 'title_es_icon'
        # content_en
        ___field___attribute___placeholder___locale___reload__(field=self.fields['content_en'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___CONTENT')
        self.fields['content_en'].widget.attrs['id'] = 'content_en'
        # content_es
        ___field___attribute___placeholder___locale___reload__(field=self.fields['content_es'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___CONTENT')
        self.fields['content_es'].widget.attrs['id'] = 'content_es'

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if self.files.get('image'):
            if len(self.files.get('image')) > 2 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_HOME___DOCUMENT___IMAGE___VALIDATION The image should not be beggear than %(weight)s.') % {'weight': '2mb', })
        return image

    def save(self, commit=True):
        instance = super(DocumentUpdate, self).save(commit=False)
        #
        if commit:
            # image
            if self.instance_current.image is not None and self.instance_current.image != '' and instance.image is not None and instance.image != '':
                if self.instance_current.image != instance.image:
                    if os.path.exists(self.instance_current.image.path):
                        os.remove(self.instance_current.image.path)
            instance.save()
        return instance


class DocumentDelete(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def ___delete___(self):
        # image
        if self.instance.image is not None and self.instance.image != '':
            if os.path.exists(self.instance.image.path):
                os.remove(self.instance.image.path)
        self.instance.delete()
