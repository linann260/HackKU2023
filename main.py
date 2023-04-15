from recipe import Recipe

def main():
    recipe_file = open('recipe.txt', 'r')
    file_list = []
    for line in recipe_file:
        file_list.append(line.strip())

    name_country = []
    line2 = []
    link = []
    
    for index in range(len(file_list) - 1):
        if index%3 == 0:
            name_country.append(file_list[index])
        elif index%3 == 1:
            line2.append(file_list[index])
        elif index%3 == 2:
            link.append(file_list[index])

    name = []
    country = []

    for item in name_country:
        item = item.split('-')
        name.append(item[0])
        country.append(item[1])

    ingredients = []

    for item in line2:
        new = item.split(',')
        ingredients.append(new)

    for index in range(len(name) - 1):
        my_recipe = Recipe(name[index], country[index], ingredients[index], link[index])
        print(my_recipe)
        
main()
