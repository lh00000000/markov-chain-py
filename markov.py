import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

nonword = "\n"
w1 = nonword
w2 = nonword

table = {}

for line in sys.stdin:
	for word in line.split():
		table.setdefault( (w1, w2), []).append(word)
		w1, w2 = w2, word

table.setdefault( (w1, w2), []).append(nonword)

w1 = nonword
w2 = nonword

maxwords = 1000

outputText = ""
for i in xrange(maxwords):
	newword = random.choice(table[(w1,w2)])
	if newword == nonword: sys.exit()
	#print newword
	outputText += " "
	outputText += newword
	w1, w2 = w2, newword

f = open('output.txt', 'w')
f.write(outputText)
f.close()
