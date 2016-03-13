from django.shortcuts import render

import forms

def tracker(request):
    request_info = {
        'repo_form': forms.RepoForm()
    }

    if request.method == 'POST':
        form = forms.RepoForm(request.POST)
        if form.is_valid():

            model_instance = form.save()
            request_info['issues'] = model_instance.get_issues()

            return render(request, 'track.html', request_info)

    return render(request, 'track.html', request_info)
