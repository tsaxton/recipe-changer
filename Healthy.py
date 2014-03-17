#!/usr/bin/env python


import recipe
import lists

def tohealthy(recipe):
	#identify protein (to remove or substitute)
	for i in range(len(recipe.ingredients)):
            ingredient = recipe.ingredients[i]
	    for ingredients in lists.healthy:
		if ingredients in ingredient["name"]:
		    recipe.ingredients[i]["name"] = lists.healthy[ingredients]
		    break



	return recipe

