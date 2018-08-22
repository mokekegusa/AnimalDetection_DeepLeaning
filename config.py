import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def json_file_load(file_path):
    f = open((os.path.join(BASE_DIR, file_path)), 'r')
    return json.load(f)
