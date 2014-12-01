import nltk
import os
import fnmatch
import html2text
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

matches = []

for root, dirnames, filenames in os.walk("./"):
	for filename in fnmatch.filter(filenames, '*.html'):
		matches.append(os.path.join(root, filename))

h = html2text.HTML2Text()
h.ignore_lines = True

corpus =""

for match in matches:
	html = open(match).read()
	corpus += h.handle(html)

print corpus