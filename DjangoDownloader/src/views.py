from django import forms
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.shortcuts import render
import subprocess

class YoutubeDLForm(forms.Form):
    url = forms.CharField(label='Youtube URL:', max_length=256)
    group = forms.CharField(label='Group:', max_length=256)
    is_video = forms.BooleanField(label='Is Video:', required=False)
    is_anime = forms.BooleanField(label='Is Anime:', required=False)

def home(request):
    # if this is a POST request we need to process the form data
    if not request.method == 'POST':
        youtube_form = YoutubeDLForm()
        return render(request, 'home.html', {'youtube_form': youtube_form})
    
def youtube_dl(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        try:
            # create a form instance and populate it with data from the request:
            form = YoutubeDLForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                command = []
                if form.cleaned_data['is_video']:
                    if form.cleaned_data['is_anime']:
                        command = ['bash', '/opt/app/YoutubeScripts/youtube-video-download', 'anime', form.cleaned_data['group'], form.cleaned_data['url']]
                    else:
                        command = ['bash', '/opt/app/YoutubeScripts/youtube-video-download', 'videos', form.cleaned_data['group'], form.cleaned_data['url']]
                else:
                    command = ['bash', '/opt/app/YoutubeScripts/youtube-music-download', form.cleaned_data['group'], form.cleaned_data['url']]
                    
                #print("Command:", ' '.join(command))
                proc = subprocess.Popen(command, shell=False)
                return HttpResponse("Downloading now...", content_type='text/plain')
        except Exception as e:
            #print("Failed Download:", repr(e))
            return HttpResponseServerError(repr(e))

