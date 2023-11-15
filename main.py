#!/usr/bin/env python3
import datetime
import os

from get_thumbnail import get_thumbnail, get_required_env

if __name__ == '__main__':
    VIDEO_ID = get_required_env("YOUTUBE_VIDEO_ID")
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H:%M:%S")
    filepath = os.path.join(os.path.dirname(__file__), f"thumbnails/{VIDEO_ID}/{date_time}.jpg")
    get_thumbnail(VIDEO_ID, filepath)
