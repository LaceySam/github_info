from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render

import urllib

import forms
from models import Repo


def tracker(request):
    """
    The tracker view, gets the first 20 items from the github issue api
    """
    request_info = {
        'repo_form': forms.RepoForm()
    }

    if request.method == 'POST':
        form = forms.RepoForm(request.POST)

        if form.is_valid():
            model_instance, created = Repo.objects.get_or_create(
                **form.cleaned_data
            )
            if not created:
                model_instance.save()

            request_info['issues'] = model_instance.get_issues()
            request_info['repo_name'] = form.cleaned_data['repo_name']

            return render(request, 'track.html', request_info)

    return render(request, 'track.html', request_info)


def get_issue_batch(request):
    """
    The get_issue_batch view gets the next 20 items from the github issue api
    """
    if request.method == "GET":
        repo_name = request.GET['repo_name']
        page = request.GET['current_page']
        repo = Repo.objects.filter(repo_name=urllib.unquote_plus(repo_name))
        if len(repo) == 0:
            return HttpResponseBadRequest

        repo = repo[0]

        return JsonResponse(repo.get_issues(int(page)+1), safe=False)

    return HttpResponseBadRequest
