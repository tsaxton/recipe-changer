import recipe
import lists

def tovegetarian(recipe):
	#identify protein (to remove or substitute)
	meats = []
	for ingredient in recipe.ingredients:
		for meat in proteins:
			if meat in ingredient["name"]:
				meats.append(ingredient)
	# remove meat from recipe
	for meat in meats:
		recipe.ingredients.remove(meat)

	return recipe





