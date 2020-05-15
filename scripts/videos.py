#!/usr/bin/env python3

import glob
import re
import sys

pattern = "movies/20*.mp4"
files = glob.glob(pattern)
files.sort(reverse=True)
regexp = r"-- (.*).mp4"
videos = []
for file in files:
    matches = re.search(regexp, file)
    if matches:
        videos.append({"title": matches.group(1),
                       "src": file})
    else:
        print("no match %s" % (file))

from mako.template import Template
mytemplate = Template(filename='templates/videos.tmpl')
print(mytemplate.render(videos=videos))
