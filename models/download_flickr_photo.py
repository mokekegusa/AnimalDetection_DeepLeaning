from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import config


# API Key
config.json_file_load('/key.json')
key = format(config['flickr']['Key'])
secret = format(config['flickr']['Secret'])


def search_filckr_photo(search_photo_str, save_dir, wait_time):
    save_dir = save_dir + search_photo_str
    flickr = FlickrAPI(key, secret, format='parsed-json')
    search_result_photos =flickr_search_params(flickr, search_photo_str, 400, 'photos', 'relevance', 1, 'url_q')
    photos = search_result_photos['photos']
    pprint(photos)

    # 関数化
    for i, photo in enumerate(photos['photo']):
        photo_download_url = photo['url_q']
        file_path = save_dir + '/' + photo['id'] + '.jpg'
        if os.path.exists(file_path):
            continue
        urlretrieve(photo_download_url, file_path)
        time.sleep(wait_time)


def flickr_search_params(flickr, search_photo_str, per_page, media, sort, safe_search, extras):
    search_result_photos = flickr.photos.search(
        text=search_photo_str,
        per_page=per_page,
        media=media,
        sort=sort,  # 検索文字列の関連順
        safe_search=safe_search,     # UIを除去
        extras=extras     # 結果に画像のURLを含む
    )
    return search_result_photos
