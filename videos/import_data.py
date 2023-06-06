import requests
from videos.models import Video

def import_videos():
    response = requests.get('https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json')
    data = response.json()

    for item in data:
        video = Video(title=item['title'], url=item['url'])
        video.save()

    print(f"Total Videos after import: {Video.objects.count()}")

# call the function to start the import process
import_videos()
