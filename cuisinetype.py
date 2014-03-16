import recipe
import lists

#main function
def changetype (recipe):
	recipe, removelist = getCusineSpecificIngredients(recipe)
	print recipe.ingredients, removelist
	


#a function that pulls out cuisine specific ingredients
def getCusineSpecificIngredients (recipe):
	cusinetype = recipe.GetCusineType()

	if cusinetype == "american":
		list = lists.american
	elif cusinetype == "asian":
		list = lists.asian
	elif cusinetype == "italian":
		list = lists.italian
	elif cusinetype == "mexican":
		list = lists. mexican

	removelist = []

	for ingredient in ingredients:
		for item in list:
			removelist.append(ingredient)

	for ingredient in removelist:
		recipe.ingredients.remove(ingredient)

	return (recipe, removelist)


#a funtion to convert TO AMERICAN

#a function to convert TO ASIAN

#a function to convert TO ITALIAN

#a function to conver TO MEXICAN

