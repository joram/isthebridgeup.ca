#!/usr/bin/env python3
import os

from googleapiclient.discovery import build
import urllib.request
from dotenv import load_dotenv

def get_required_env(name: str):
    value = os.environ.get(name)
    if value is None:
        raise Exception(f"missing environment variable {name}")
    return value


load_dotenv()
API_KEY = get_required_env("YOUTUBE_API_KEY")


def get_thumbnail(video_id: str, filepath: str):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    response = youtube.videos().list(part='snippet', id=video_id).execute()
    thumbnail_url = response['items'][0]['snippet']['thumbnails']['high']['url']
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    urllib.request.urlretrieve(thumbnail_url, filepath)
    print('Thumbnail downloaded successfully.')

