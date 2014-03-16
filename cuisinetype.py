import recipe
import lists

#main function
def changetype (recipe):
	recipe, removelist = getCuisineSpecificIngredients(recipe)
	print recipe.ingredients, removelist
	


#a function that pulls out cuisine specific ingredients
def getCuisineSpecificIngredients (recipe):
	cuisinetype = recipe.getCuisineType()

	if cuisinetype == "american":
		inglist = lists.american
	elif cuisinetype == "asian":
		inglist = lists.asian
	elif cuisinetype == "italian":
		inglist = lists.italian
	elif cuisinetype == "mexican":
		inglist = lists.mexican

	removelist = []

	for ingredient in recipe.ingredients:
		for item in inglist:
			if item.lower().strip() in ingredient['name'].lower().strip():
			    removelist.append(ingredient)
			    break

	for ingredient in removelist:
		recipe.ingredients.remove(ingredient)

	return (recipe, removelist)


#a funtion to convert TO AMERICAN

#a function to convert TO ASIAN

#a function to convert TO ITALIAN

#a function to conver TO MEXICAN

