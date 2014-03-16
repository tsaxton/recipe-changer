#!/usr/bin/env python


import recipe
import lists

def tohealthy(recipe):
	#identify protein (to remove or substitute)
	meats = []
	for ingredient in recipe.ingredients:
		for ingredients in lists.healthy:
			if ingredients in ingredient["name"]:
				ingredient["name"] = lists.healthy[ingredients]
				break



	return recipe

