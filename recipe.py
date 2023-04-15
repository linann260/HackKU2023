class Recipe:

    def __init__(self, name, country, ingredients, link):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.link = link

    def __str__(self):
        return (f"{self.name} - {self.country}\nIngredients: {self.ingredients}\nLink: {self.link}")
