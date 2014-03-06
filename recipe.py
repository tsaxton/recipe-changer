import BeautifulSoup as bs
import urllib2

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
        	self.ingredients[i]['amount'] = ing.find('span', {'class': 'ingredient-amount'}).string
        	self.ingredients[i]['name'] = ing.find('span', {'class': 'ingredient-name'}).string
        	i += 1
        return self.ingredients

