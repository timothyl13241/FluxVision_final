#!/usr/bin/python3
# -*- coding: utf-8 -*-
import youtube_dl
import sys
import os
import pickle
import time

abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

def get_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': abs_path + 'video.mp4',
        'noplaylist': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    url = sys.argv[1]
    get_video(url)
