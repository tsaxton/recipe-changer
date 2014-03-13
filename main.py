import recipe
import pprint
import sys
url = sys.argv[1]
a = recipe.recipe(url)
pprint.pprint(a.getIngredients())
pprint.pprint(a.getSteps())
pprint.pprint(a.getTools())
print(a.getPrimaryMethod())
a.getJSON()
