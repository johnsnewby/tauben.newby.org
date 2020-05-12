#!/bin/sh

ffmpeg -hide_banner -loglevel error -i http://tauben.local:8081  -frames 1 -vcodec copy /home/newby/Pictures/Pigeons/snapshot`date +%Y%m%d%H%M%S`.jpg
