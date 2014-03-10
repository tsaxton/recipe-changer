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
        ''' Constructor takes a URL from allrecipes.com and loads it.
            Returns recipe object '''
        self.url = url
        
        conn = urllib2.urlopen(url)
        self.html = conn.read()
        self.getSteps()
        self.getIngredients()
        self.getTools()

    def getIngredients(self):
        ''' getIngredients parses the ingredients from the page's HTML, then
            tries to find quantity, measurement, and descriptors
            INPUTS: recipe object
            OUTPUTS: dictionary of ingredients and their attributes '''
        if len(self.ingredients) > 0:
        	return self.ingredients # already got ingredients, just need to return them
        soup = bs.BeautifulSoup(self.html)
        ingredients = soup('li', {'id': 'liIngredient'}) # find the ingredient list
        i = 0
        for ing in ingredients:
        	self.ingredients.append({})
        	amount = ing.find('span', {'class': 'ingredient-amount'}).string # the amount is in its own span
        	amount = amount.split(" ")
            # split amount into quantity and measurement
        	if len(amount) == 1:
        		self.ingredients[i]['quantity'] = amount[0]
        		self.ingredients[i]['measurement'] = ''
        	elif len(amount) == 2:
        	    self.ingredients[i]['quantity'] = amount[0]
        	    self.ingredients[i]['measurement'] = amount[1]
        	if not self.ingredients[i]['quantity'].isdigit(): # transform 1/2 into .5 and etc. TODO: make it handle things like 1-1/2 or 1 1/2.
        		if len(self.ingredients[i]['quantity'].split('/')) == 2:
        			vals = self.ingredients[i]['quantity'].split('/')
        			self.ingredients[i]['quantity'] = float(vals[0])/float(vals[1])
        	name = ing.find('span', {'class': 'ingredient-name'}).string # get ingredient name
        	name2 = "".join(l for l in name if l not in string.punctuation)
        	nameArr = name2.split(' ')
        	descriptors = []
        	nameArr2 = []
        	for word in nameArr:
        		if word in lists.descriptors:
        			descriptors.append(word) # add the descriptor to descriptors
        		else:
        			nameArr2.append(word)
        	desc = '' # convert descriptors from array to string
        	for j in range(len(descriptors)):
        		desc += descriptors[j]
        		if j != len(descriptors)-1:
        			desc += ' '
        	self.ingredients[i]['descriptor'] = desc # save descriptors
        	name = ''
        	for j in range(len(nameArr2)):
        		name += nameArr2[j]
        		if j != len(nameArr2)-1:
        			name += ' '
        	self.ingredients[i]['name'] = name # save name
        	i += 1
        return self.ingredients

    def getSteps(self):
        ''' Parses the HTML for the recipe site and gets the recipe steps as defined there
            INPUTS: recipe object
            OUTPUTS: list of steps'''
        if len(self.steps) > 0:
        	return self.steps # already got steps, just need to return them
        soup = bs.BeautifulSoup(self.html)
        directions = soup.find('div', {'class': 'directions'}) # tries to find the area directions are in
        directions = directions.find('ol') # the steps are in an ordered list
        steps = directions('li') # each step is its own list item
        for step in steps:
        	self.steps.append(step.find('span').string) # append the string (the step) to the steps list
        return self.steps # return the steps, which are also saved in the object

    def getPrimaryMethod(self):
        ''' Uses rudimentary method to determine the primary cooking method and returns it.
            INPUTS: recipe object
            OUTPUTS: string containing primary cooking method'''
	    if len(self.steps) == 0: # if we don't already have the steps loaded, get them
	    	self.getSteps()
	    for i in reversed(range(len(self.steps))): # starting from the last step
	    	for method in lists.primaryCookingMethods: # look for a primary cooking method
	    		if method in self.steps[i].lower():
	    			return method # if one is found, return it
	    return None # if none is found, don't return anything

    def getTools(self):
        ''' Reads through the steps and finds tool words in them. Creates a list of the tools
            mentioned in the steps
            INPUTS: recipe object
            OUTPUTS: list of tools'''
        if len(self.tools) > 0:
        	return self.tools # already got the tools, just need to return them
        if len(self.steps) == 0:
        	self.getSteps()
        for s in self.steps:
        	tokens = nltk.word_tokenize(s) # tokenize the steps into words
        	bigram = bigrams(tokens) # and bigrams too, since some tools are two words
        	for t in tokens: # now making list of tools
        		t = t.strip().lower()
        		if t in lists.tools:
        			self.tools.append(t)
        	for t in bigram:
        		t = t[0] + " " + t[1]
        		t = t.strip().lower()
        		if t in lists.tools:
        			self.tools.append(t)
        self.tools = list(set(self.tools))
        return self.tools # return list of tools
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
