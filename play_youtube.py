#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import subprocess

abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

if __name__ == '__main__':
    video_file = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else "Unknown title"
    # Write title to file for ticker
    with open(abs_path + ".title_txt", "w") as tf:
        tf.write(title)
    # Play video
    subprocess.call(["omxplayer", video_file])