from recipeDAO import recipe_dao


print("test recipeDAO")
# This is a test script for the recipeDAO class, which interacts with a MySQL database to manage recipes.

recipes = {
    "name": "Banana Bread",
    "meal_type": "Snack",
    "ingredients_count": 8,
    "ingredients_list": """3-4 ripe Bananas, 
                            340g flour, 
                            170g sugar, 
                            70g dairy free butter, 
                            1 egg, 
                            1 tbs baking powder, 
                            pinch of salt, 
                            1 tbsp vanilla""",
    "time": "1 hour 10 minutes",
    "method": """1. Preheat oven to 175°C.
                 2. Mix the butter and Bananas.
                 3. Mix the sugar, egg, and vanilla.
                 4. Add the salt, baking powder, and flour and mix well.
                 5. Pour into a loaf tin and bake for 1 hour.
                 6. Leave to cool for 10 mins before removing from the tin."""
}
# create a new recipe
print("\n Creating a new recipe")
recipe = recipe_dao.create(recipes)
recipes_id = recipe["id"]
print("Created with ID: ", recipes_id)


#find by id
print("\n Finding the recipe by ID")
result = recipe_dao.findByID(recipes_id)
print ("Found recipe:")
print (result)

#update
new_recipes_value = {
    "name": "Banana Bread with Walnuts",
    "meal_type": "Snack",
    "ingredients_count": 9,
    "ingredients_list": """3-4 ripe Bananas, 
                            340g flour, 
                            170g sugar, 
                            70g dairy free butter, 
                            1 egg, 
                            1 tbs baking powder, 
                            pinch of salt, 
                            1 tbsp vanilla,
                            100g walnuts""",
"time": "1 hour 20 minutes",
"method": """1. Preheat oven to 175°C.
                 2. Mix the butter and Bananas.
                 3. Mix the sugar, egg, and vanilla.
                 4. Add the salt, baking powder, flour and walnuts and mix well.
                 5. Pour into a loaf tin and bake for 1 hour.
                 6. Leave to cool for 10 mins before removing from the tin."""}
print("\n Updating the recipe")
recipe_dao.update(recipes_id, new_recipes_value)
print("Recipe updated", recipes_id)
print(result)
print("🔧 With values:")

#get all
print("\n get all Recipes")
all_recipes = recipe_dao.getAll()
for recipes in all_recipes:
    print(recipes)

#delete
# recipe_dao.delete(recipes_id)
# print("Deleting recipe ID:", id)
print("\n Test complete")