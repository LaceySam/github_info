from django.shortcuts import render

def tracker(request):
    request_info = {}

    return render(request, 'track.html', request_info)
