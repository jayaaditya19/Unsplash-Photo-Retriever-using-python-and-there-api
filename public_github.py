import requests
import urllib.request as url

query = input("Enter a search query: ")
link = 'https://api.unsplash.com/search/photos/?query=' + query + '&per_page=1&client_id=YOURCLIENTID'

r = requests.get(link)
data = r.json()
data.keys()
data['results']

for image_data in data['results']:
    file_name = str(image_data['id']) + '.jpg'
    image_url = image_data['urls']['raw']
    print(image_url)
    url.urlretrieve(image_url, file_name)