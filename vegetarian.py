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

	return recipe





