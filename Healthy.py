#!/usr/bin/env python

import recipe
import lists

def tohealthy(recipe):
	#identify protein (to remove or substitute)
	meats = []
	for ingredient in recipe.ingredients:
		for meat in lists.healthy:
			if meat in ingredient["name"]:
				meats.append(ingredient)
				break
	# remove meat from recipe
	for meat in meats:
		print meat
		recipe.ingredients.remove(meat)


	type = recipe.getCuisineType()

	if type == "american":
		recipe.ingredients.append({'name':'mushroom'})
	elif type == "italian":
		recipe.ingredients.append({'name':'eggplant'})
	elif type == "asian":
		recipe.ingredients.append({'name':'tofu'})
	elif type == "mexican":
		recipe.ingredients.append({'name':'peppers'})



	return recipe
