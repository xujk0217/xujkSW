from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def main(request):
    return render(request, 'main.html')

def app_ads_txt(request):
    """Serve app-ads.txt file"""
    # Hardcoded content for app-ads.txt
    content = "google.com, pub-4105005748617921, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(content, content_type='text/plain')