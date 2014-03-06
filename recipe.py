import BeautifulSoup as bs
import urllib2
import lists
import string

class recipe:
    ingredients = []

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

