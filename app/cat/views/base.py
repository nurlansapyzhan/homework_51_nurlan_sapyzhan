from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def main_page(request: WSGIRequest):
    return render(request, 'main_page.html')
