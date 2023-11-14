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
VIDEO_ID= get_required_env("YOUTUBE_VIDEO_ID")


def get_thumbnail():
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    response = youtube.videos().list(part='snippet', id=VIDEO_ID).execute()
    thumbnail_url = response['items'][0]['snippet']['thumbnails']['high']['url']
    urllib.request.urlretrieve(thumbnail_url, 'live_stream_thumbnail.jpg')
    print('Thumbnail downloaded successfully.')

get_thumbnail()
