#!/bin/bash

cd /home/newby/Pictures/Pigeons/movie
. venv/bin/activate
./create.py
rsync -avz 2020*.mp4 door.newby.org:mjpeg/html/movies
