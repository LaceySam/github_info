from django import forms
from django.conf import settings

import models


class RepoForm(forms.ModelForm):
    class Meta:
        model = models.Repo
        fields = ['repo_name']
        widgets = {
            'repo_name': forms.TextInput(
                attrs={
                    'size': settings.DEFAULT_FORM_SIZE,
                    'placeholder': settings.DEFAULT_REPO
                }
            )
        }

    def clean_repo_name(self):
        repo_name = self.cleaned_data['repo_name']

        if repo_name == '':
            repo_name = settings.DEFAULT_REPO

        if not repo_name.endswith('/'):
            repo_name = repo_name + '/'

        return repo_name
