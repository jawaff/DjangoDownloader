import os
import sys
from django.urls import include, path
from django.shortcuts import render
from django.core.wsgi import get_wsgi_application

from src import views

os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = False
SECRET_KEY = '__secret_key__'
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = __name__
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')]
}]

urlpatterns = [
    path('', views.home),
    path('youtube-download/', views.youtube_dl),
]

if DEBUG:
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
else:
    import netius.servers
    application = get_wsgi_application()
    server = netius.servers.WSGIServer(app=application)
    server.serve(host='0.0.0.0', port=8080)
