import recipe
import pprint
import sys
import vegetarian
import healthy
url = sys.argv[1]
a = recipe.recipe(url)
pprint.pprint(a.getIngredients())
pprint.pprint(a.getSteps())
a = vegetarian.tovegetarian(a)
print a.getCuisineType()
pprint.pprint(a.getIngredients())
a = a.healthy.tohealthy(a)
pprint.pprint(a.getIngredients)
#pprint.pprint(a.getSteps())
#pprint.pprint(a.getTools())
#print(a.getPrimaryMethod())
#a.getJSON()
