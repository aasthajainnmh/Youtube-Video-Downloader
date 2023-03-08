from django.shortcuts import render,redirect
from pytube import *

def youtube(request):
    if request.method=='POST':
        # Getting link from frontend
        link=request.POST['link']
        video=YouTube(link)
        
        # setting video resolution
        stream=video.streams.get_lowest_resolution()
        
        # Download video
        stream.download()
        
        # Returning HTML page
        return render(request,'youtube.html')
    return render(request,'youtube.html')