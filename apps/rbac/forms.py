# -*- coding: UTF-8 -*-

from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    position = forms.IntegerField(required=False)

    def clean(self):
        url = self.cleaned_data.pop('url', None)
        position = self.cleaned_data.pop('position', 0)
        if url:
            self.cleaned_data['url'] = url
        if not position:
            self.cleaned_data['position'] = 0
        else:
            self.cleaned_data['position'] = position
        return self.cleaned_data
