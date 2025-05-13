from recipeDAO import recipe_DAO

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
#create
recipe = recipe_DAO.create(recipes)
recipes_id = recipes["id"]

#find by id
result = recipe_DAO.findById(recipes_id)
print ("test create and find by id")
print (result)

#update
newrecipesvalue = {
    "name": "Banana Bread with Walnuts",
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
recipe_DAO.update(recipes_id, newrecipesvalue)
print("test update")
print(result)

#get all
print("test get all")
all_recipes = recipe_DAO.getAall()
for recipes in all_recipes:
    print(recipes)

#delete
recipe_DAO.delete(recipes_id)