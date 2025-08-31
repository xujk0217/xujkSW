from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def main(request):
    return render(request, 'main.html')

def app_ads_txt(request):
    """Serve app-ads.txt file"""
    file_path = os.path.join(settings.BASE_DIR, 'app-ads.txt')
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse('File not found', status=404)