from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    print(f"Videos before filter: {videos.count()}")
    title_query = request.GET.get('title')
    if title_query:
        videos = videos.filter(title__icontains=title_query)
    print(f"Videos after filter: {videos.count()}")
    return render(request, 'videos/video_list.html', {'videos': videos})
