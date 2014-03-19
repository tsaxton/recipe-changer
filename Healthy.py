#!/usr/bin/env python


import recipe
import lists

def tohealthy(recipe):
        for i in range(len(recipe.steps)):
            method = recipe.steps[i]
	    if recipe.getPrimaryMethod() == "Stir-Fry":
		    for i in range(len(recipe.ingredients)):
			ingredient = recipe.ingredients[i]
			if "oil" in ingredient["name"]:
				recipe.swapStepIngredients(recipe.ingredients[i]["name"], "Vegetable Broth")
				ingredient["name"] = "Vegetable Broth"
				ingredient["quantity"] = .5
				ingredient["measurement"] = "cups"
				break
            for methods in lists.healthymethods:
			
                if methods in method["action"]:
		    recipe.swapStepMethod(recipe.steps[i]["action"], lists.healthymethods[methods])
                    recipe.steps[i]["action"] = lists.healthymethods[methods]
		    recipe.steps[i]["time"] = "15-25 minutes or until cooked through"
                    recipe.steps[i]["tools"] = ["baking pan"]
		    recipe.steps.insert(0, {"action":"preheat oven to 450", "tools":["Oven"], "ingredients":[], "time":""})
                    recipe.primarymethod = "Bake"
		    break
        
	#identify protein (to remove or substitute)
	for i in range(len(recipe.ingredients)):
            ingredient = recipe.ingredients[i]
	    for ingredients in lists.healthy:
		if "broth" in ingredient["name"]:
			break
		elif "soup" in ingredient["name"]:
			break
			
		elif ingredients in ingredient["name"]:
			recipe.swapStepIngredients(recipe.ingredients[i]["name"],lists.healthy[ingredients])
			recipe.ingredients[i]["name"] = lists.healthy[ingredients]
			break
		if "cheese" in ingredient["name"]:
			if recipe.ingredients[i]["quantity"]:
				recipe.ingredients[i]["quantity"] = recipe.ingredients[i]["quantity"]/2
				break
	## cut down unhealthy ingredient amounts
	## caramelizing
	## stir fry no oil
	## cut down pasta and increase veggies
	## cut out mayo
	## salad dressings - blue cheese, marinades
	## couple table spoons of broth can be used for oil in stir fry

	return recipe

