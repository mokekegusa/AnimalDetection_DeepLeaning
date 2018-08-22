from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = open((os.path.join(BASE_DIR, 'key.json')), 'r')
Flickr_API = json.load(f)

# API Key
key = format(Flickr_API['flickr']['Key'])
secret = format(Flickr_API['flickr']['Secret'])
wait_time = 1.0

search_photo_str = sys.argv[1]
save_dir = '.././images/' + search_photo_str

flickr = FlickrAPI(key, secret, format='parsed-json')
search_result_photos = flickr.photos.search(
    text=search_photo_str,
    per_page=400,
    media='photos',
    sort='relevance',  # 検索文字列の関連順
    safe_search=1,     # UIを除去
    extras='url_q'     # 結果に画像のURLを含む
)

photos = search_result_photos['photos']
pprint(photos)

for i, photo in enumerate(photos['photo']):
    photo_download_url = photo['url_q']
    file_path = save_dir + '/' + photo['id'] + '.jpg'
    if os.path.exists(file_path):
        continue
    urlretrieve(photo_download_url, file_path)
    time.sleep(wait_time)
