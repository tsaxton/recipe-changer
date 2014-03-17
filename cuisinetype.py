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
def toAmerican (recipe, removelist):
	for ingredient in removelist:
		for item in list.equivalencies:
			if item["asian"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["american"])
				break
			if item["italian"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["american"])
				break
			if item["mexican"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["american"])
				break

	return recipe
				
#a function to convert TO ASIAN
def toAsian (recipe, removelist):
	for ingredient in removelist:
		for item in list.equivalencies:
			if item["american"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["asian"]})
				break
			if item["italian"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["asian"]})
				break
			if item["mexican"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["asian"]})
				break

	return recipe
				


#a function to convert TO ITALIAN
def toItalian (recipe, removelist):
	for ingredient in removelist:
		for item in list.equivalencies:
			if item["asian"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["italian"]})
				break
			if item["american"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["italian"]})
				break
			if item["mexican"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["italian"]})
				break

	return recipe


#a function to conver TO MEXICAN
def toMexican (recipe, removelist):
	for ingredient in removelist:
		for item in list.equivalencies:
			if item["american"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["mexican"]})
				break
			if item["italian"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["mexican"]})
				break
			if item["asian"] in ingredient["name"]:
				recipe.ingredients.append({"name":item["mexican"]})
				break

	return recipe


