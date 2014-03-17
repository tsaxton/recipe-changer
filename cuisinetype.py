import recipe
import lists

#main function
def changetype (recipe):
    recipe, removelist = getCuisineSpecificIngredients(recipe)
    recipe = toAmerican(recipe, removelist)
    return recipe
    


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
        print ingredient['name']
        for item in lists.equivalencies:
            if item["asian"] in ingredient["name"].lower():
                if item['asian'] == '':
                    continue
                print item
                recipe.ingredients.append({"name":item["american"]})
                break
            elif item["italian"] in ingredient["name"].lower():
                if item['italian'] == '':
                    continue
                print item
                recipe.ingredients.append({"name":item["american"]})
                break
            elif item["mexican"] in ingredient["name"].lower():
                if item['mexican'] == '':
                    continue
                print item
                recipe.ingredients.append({"name":item["american"]})
                break

    return recipe
                
#a function to convert TO ASIAN
def toAsian (recipe, removelist):
    for ingredient in removelist:
        print ingredient['name']
        for item in lists.equivalencies:
            if item["american"] in ingredient["name"].lower():
                if item['american'] == '':
                    continue
                print item
                recipe.ingredients.append({"name":item["asian"]})
                break
            if item["italian"] in ingredient["name"].lower():
                if item['italian'] == '':
                    continue
                print item
                recipe.ingredients.append({"name":item["asian"]})
                break
            if item["mexican"] in ingredient["name"].lower():
                if item['mexican'] == '':
                    continue
                print item
                recipe.ingredients.append({"name":item["asian"]})
                break

    return recipe
                


#a function to convert TO ITALIAN
def toItalian (recipe, removelist):
    for ingredient in removelist:
        for item in lists.equivalencies:
            if item["asian"] in ingredient["name"].lower():
                if item['asian'] == '':
                    continue
                recipe.ingredients.append({"name":item["italian"]})
                break
            if item["american"] in ingredient["name"].lower():
                if item['american'] == '':
                    continue
                recipe.ingredients.append({"name":item["italian"]})
                break
            if item["mexican"] in ingredient["name"].lower():
                if item['mexican'] == '':
                    continue
                recipe.ingredients.append({"name":item["italian"]})
                break

    return recipe


#a function to conver TO MEXICAN
def toMexican (recipe, removelist):
    for ingredient in removelist:
        for item in lists.equivalencies:
            if item["american"] in ingredient["name"].lower():
                if item['american'] == '':
                    continue
                recipe.ingredients.append({"name":item["mexican"]})
                break
            if item["italian"] in ingredient["name"].lower():
                if item['italian'] == '':
                    continue
                recipe.ingredients.append({"name":item["mexican"]})
                break
            if item["asian"] in ingredient["name"].lower():
                if item['asian'] == '':
                    continue
                recipe.ingredients.append({"name":item["mexican"]})
                break

    return recipe


