import requests

response = requests.get('https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json')
data = response.json()

for item in data:
    print(item)
