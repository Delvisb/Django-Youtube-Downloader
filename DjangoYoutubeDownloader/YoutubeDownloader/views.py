from django.shortcuts import render
from django.views import View
from django.http import FileResponse
from pytube import *

# Create your views here.
def home(request):

    return render(request, 'home.html')

class download(View): 
    def __init__(self, url = None):
        self.url = url 

    def get(self, request):
        return render(request, 'download.html')

    def post(self, request):
        if request.POST.get('searchVideo'):
            try:
                videourl = request.POST['videourl']
                video = YouTube(videourl)
                thumbnail, title, views, author= video.thumbnail_url, video.title, video.views, video.author
                result = video.streams.get_highest_resolution()
                filename = title.replace(" ", "") + ".mp4"
                result.download(output_path='YoutubeDownloader/downloads', filename= filename)
                context= {
                    'status': '200',
                    'thumbnail': thumbnail,
                    'title': title,
                    'views': views,
                    'author': author,
                    'filename': filename
                }
                return render(request, 'download.html', { 'context': context})
            except Exception as e:
                print(e)
                context= { 'status': '500' }
                return render(request, 'download.html', {'context': context})

def viewVideo(request, file):
    filename = f"./YoutubeDownloader/downloads/{file}"
    print(filename)
    response = FileResponse(open(filename, 'rb'))
    return response
