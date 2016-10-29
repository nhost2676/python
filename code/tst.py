 #-*- coding: utf8 -*-
#import sys
#import codecs
#writer_factory = codecs.getwriter("utf-8")
#sys.stdout = writer_factory(sys.stdout)

import urllib

import re

url = urllib.urlopen("https://www.youtube.com/watch?v=ISzaAWBdZyo")
s = url.read()

regex = '<title>(.+?)</title>'
reg = re.compile(regex)
title = re.findall(reg, str(s))
title = title
print title
#print s
#print s.__len__()

print "Giowf in được ko"