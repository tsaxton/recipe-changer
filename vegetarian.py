import recipe
import lists

def tovegetarian(recipe):
	#identify protein (to remove or substitute)
	meats = []
	for ingredient in recipe.ingredients:
		for meat in lists.proteins:
			if meat in ingredient["name"]:
				meats.append(ingredient)
				break
	# remove meat from recipe
	for meat in meats:
		print meat
		recipe.ingredients.remove(meat)


	type = recipe.getCuisineType()

	for meat in meats:
	    liquid = False
	    for liquid in lists.liquids:
	    	liquid = True
	    if liquid == True:
	    	recipe.ingredients.append({'name': 'vegetable broth', 'descriptor': '', 'measurement': meat['measurement'], 'quantity': meat['quantity'], 'preparation': ''})
	    elif type == "american":
		    recipe.ingredients.append({'name':'mushroom', 'descriptor': '', 'measurement': meat['measurement'], 'quantity': meat['quantity'], 'preparation': meat['preparation']})
	    elif type == "italian":
		    recipe.ingredients.append({'name':'eggplant', 'descriptor': '', 'measurement': meat['measurement'], 'quantity': meat['quantity'], 'preparation': meat['preparation']})
	    elif type == "asian":
		    recipe.ingredients.append({'name':'tofu', 'descriptor': '', 'measurement': meat['measurement'], 'quantity': meat['quantity'], 'preparation': meat['preparation']})
	    elif type == "mexican":
		    recipe.ingredients.append({'name':'peppers', 'descriptor': '', 'measurement': meat['measurement'], 'quantity': meat['quantity'], 'preparation': 'chopped'})



	return recipe





