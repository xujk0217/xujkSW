from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def main(request):
    return render(request, 'main.html')

def app_ads_txt(request):
    """Serve app-ads.txt file"""
    # Try multiple possible paths for the file
    possible_paths = [
        os.path.join(settings.BASE_DIR, 'app-ads.txt'),
        os.path.join(settings.BASE_DIR, 'public', 'app-ads.txt'),
        'app-ads.txt',
        'public/app-ads.txt'
    ]
    
    for file_path in possible_paths:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return HttpResponse(content, content_type='text/plain')
        except FileNotFoundError:
            continue
    
    return HttpResponse('File not found', status=404)