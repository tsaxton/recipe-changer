#!/usr/bin/env python


import recipe
import lists

def tohealthy(recipe):
        #change cooking method to healthy alternative
	##need to change primary method tag
        for i in range(len(recipe.steps)):
            method = recipe.steps[i]
            for methods in lists.healthy:
                if methods in method["action"]:
		    recipe.swapStepMethod(recipe.steps[i]["action"], lists.healthy[methods])
                    recipe.steps[i]["action"] = lists.healthy[methods]
		    recipe.steps[i]["time"] = "15-25 minutes or until cooked through"
                    recipe.steps[i]["tools"] = ["baking pan"]
                    break
        
	#identify protein (to remove or substitute)
	for i in range(len(recipe.ingredients)):
            ingredient = recipe.ingredients[i]
	    for ingredients in lists.healthy:
		if ingredients in ingredient["name"]:
			recipe.swapStepIngredients(recipe.ingredients[i]["name"],lists.healthy[ingredients])
			recipe.ingredients[i]["name"] = lists.healthy[ingredients]
			break
	## cut down unhealthy ingredient amounts
	## caramelizing
	## stir fry no oil
	## cut down pasta and increase veggies
	## cut out mayo
	## swap mozarella for skim ricotta
	## salad dressings - blue cheese, marinades
	## couple table spoons of broth can be used for oil in stir fry

	return recipe

