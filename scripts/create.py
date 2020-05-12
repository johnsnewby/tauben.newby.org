#!/usr/bin/env python3

from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
import glob
import re
import subprocess
import sys

city = LocationInfo("Berlin", "Germany", "52.5", "13.4")

if len(sys.argv) == 2:
    _date = sys.argv[1]
else:
    _now = datetime.today() - timedelta(days=1)
    _date = "%d%02d%02d" % (_now.year, _now.month, _now.day)

date = datetime.strptime(_date, "%Y%m%d")
output_file = date.strftime("%Y%m%d -- %A%e %B.mpg")
events = sun(city.observer, date)
sunrise = events['sunrise']
sunset = events['sunset']

def is_daylight(hour, minute):
    if hour < sunrise.hour-1:
        return False
    if hour > sunset.hour+1:
        return False
    return True

pattern = "../snapshot%s*.jpg" % (_date)
print(pattern)
files = glob.glob(pattern)
files.sort()
ffmpeg_command = "ffmpeg -f image2pipe -c:v mjpeg -i -"
ffmpeg_command = ffmpeg_command.split()
ffmpeg_command.append(output_file)

regex = r"snapshot(\d\d\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d).jpg"
daylight_files = []
for file in files:
    matches = re.search(regex, file)
    if matches:
        hour = int(matches.group(4))
        minute = int(matches.group(5))
        if is_daylight(hour, minute):
            daylight_files.append(file)

proc = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)
for file in daylight_files:
    f = open(file, "rb")
    contents = f.read()
    proc.stdin.write(contents)

proc.stdin.close()
