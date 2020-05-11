#!/usr/bin/env python3

from mako.template import Template
mytemplate = Template(filename='videos.tmpl')
print(mytemplate.render())
