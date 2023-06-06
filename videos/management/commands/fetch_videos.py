import requests
from django.core.management.base import BaseCommand
from videos.models import Video

class Command(BaseCommand):
    help = "Fetches video data from the API"

    def handle(self, *args, **options):
        url = 'https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json'
        response = requests.get(url)
        data = response.json()

        for item in data:
            title = item.get('name')
            description = item.get('description', '')  # Set a default value if description is not available
            video_uri = item.get('manifestUri')
            icon_uri = item.get('iconUri')

            try:
                video = Video.objects.get(title=title)
                video.description = description
                video.video_uri = video_uri
                video.icon_uri = icon_uri
                video.save()
            except Video.DoesNotExist:
                if description:
                    Video.objects.create(
                        title=title,
                        description=description,
                        video_uri=video_uri,
                        icon_uri=icon_uri
                    )

