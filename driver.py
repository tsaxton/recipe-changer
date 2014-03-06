import recipe

a = recipe.recipe('http://allrecipes.com/Recipe/Blackened-Chicken/Detail.aspx?soid=recs_recipe_4')
print a.getIngredients()
