from django import forms

from django.conf import settings

class RepoForm(forms.Form):
    repo_name = forms.CharField(
        label='Repo Name',
        max_length=settings.DEFAULT_FORM_CHAR_LIMIT,
        widget=forms.TextInput(
            attrs={
                'size': settings.DEFAULT_FORM_SIZE,
                'placeholder': settings.DEFAULT_REPO
            }
        )
    )
