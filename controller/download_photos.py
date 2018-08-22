import sys

from models.download_flickr_photo import search_filckr_photo


wait_time = 1.0

save_dir = 'images/'

search_photo_str = sys.argv[1]
search_filckr_photo(search_photo_str, save_dir, wait_time)
