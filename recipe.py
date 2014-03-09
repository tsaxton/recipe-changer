import bs4 as bs
import urllib2
import lists
import string
import nltk
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams, trigrams
import math

class recipe:
    ingredients = []
    steps = []
    tools = []

    def __init__(self, url):
        self.url = url
        
        conn = urllib2.urlopen(url)
        self.html = conn.read()

    def getIngredients(self):
        soup = bs.BeautifulSoup(self.html)
        ingredients = soup('li', {'id': 'liIngredient'})
        i = 0
        for ing in ingredients:
        	self.ingredients.append({})
        	amount = ing.find('span', {'class': 'ingredient-amount'}).string
        	amount = amount.split(" ")
        	if len(amount) == 1:
        		self.ingredients[i]['quantity'] = amount[0]
        		self.ingredients[i]['measurement'] = ''
        	elif len(amount) == 2:
        	    self.ingredients[i]['quantity'] = amount[0]
        	    self.ingredients[i]['measurement'] = amount[1]
        	if not self.ingredients[i]['quantity'].isdigit():
        		if len(self.ingredients[i]['quantity'].split('/')) == 2:
        			vals = self.ingredients[i]['quantity'].split('/')
        			self.ingredients[i]['quantity'] = float(vals[0])/float(vals[1])
        	name = ing.find('span', {'class': 'ingredient-name'}).string
        	name2 = "".join(l for l in name if l not in string.punctuation)
        	print name2
        	nameArr = name2.split(' ')
        	descriptors = []
        	nameArr2 = []
        	for word in nameArr:
        		if word in lists.descriptors:
        			descriptors.append(word)
        		else:
        			nameArr2.append(word)
        	desc = ''
        	for j in range(len(descriptors)):
        		desc += descriptors[j]
        		if j != len(descriptors)-1:
        			desc += ' '
        	self.ingredients[i]['descriptor'] = desc
        	name = ''
        	for j in range(len(nameArr2)):
        		name += nameArr2[j]
        		if j != len(nameArr2)-1:
        			name += ' '
        	self.ingredients[i]['name'] = name
        	i += 1
        return self.ingredients

    def getSteps(self):
        soup = bs.BeautifulSoup(self.html)
        directions = soup.find('div', {'class': 'directions'})
        directions = directions.find('ol')
        steps = directions('li')
        for step in steps:
        	self.steps.append(step.find('span').string)
        return self.steps

    def getTools(self):
        if len(self.steps) == 0:
        	self.getSteps()
        for s in self.steps:
        	tokens = nltk.word_tokenize(s)
        	bigram = bigrams(tokens)
        	for t in tokens:
        		t = t.strip().lower()
        		if t in lists.tools:
        			self.tools.append(t)
        	for t in bigram:
        		t = t[0] + " " + t[1]
        		t = t.strip().lower()
        		if t in lists.tools:
        			self.tools.append(t)
		#### This section is for making the program able to add previously unseen ingredients to its growing library
		#for x in range(len(tokens)):
		#    if (tokens[x] == "a"):
		#	add = (tokens[x+1:x+4])
		#	add = bigrams(add)
		#	for t in add:
		#	    t = t[0] + " " + t[1]
		#	    t = t.strip().lower()
		#	    t = RePunc(t)
		#	    if t not in lists.tools:
		#		print "Unrecognized input: ", t
		#		Answer = raw_input("Should this be added to a list (Y/N)? \n")
		#		if (Answer == 'y' or 'Y' ):
		#		    Category = raw_input("Should this be added to:\n(t) tools\n(s) spices\n(p) proteins?")
		#	self.tools.append(add)
        return self.tools
    
def RePunc(strang):
    words =str(strang)
    words = words.translate(None, ',')
    words = words.translate(None, '"')
    words = words.translate(None, '.')
    words = words.translate(None, '...')
    words = words.translate(None, '?')
    words = words.translate(None, '!')
    words = words.translate(None, ';')
    words = words.translate(None, '-')
    words = words.translate(None, '\'')
    words = words.translate(None, '.\'')
    words = words.translate(None, '(')
    words = words.translate(None, ')')
    words = words.translate(None, ':')
    return(words)