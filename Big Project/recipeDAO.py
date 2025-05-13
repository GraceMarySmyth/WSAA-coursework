import mysql.connector
import dbconfig as cfg
class recipeDAO:
    connection=""
    cursor =''
    host=       'localhost'
    user=       'root'
    password=   ''
    database=   'smyth_family_recipes'
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']
        self.connection = None
        self.cursor = None
# get a cursor to the database
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

# close the connection and cursor- for cleanup and avoiding leaks.
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

 # get all recipes   
    def getAll(self):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM recipes")
        results = cursor.fetchall()
        return_array = [self.convertToDictionary(row) for row in results]
        self.closeAll()
        return return_array

# get one recipe by id as a dict
    def findByID(self, id):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM recipes WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDictionary(result) if result else {}

#the recipe just created as a dict
    def create(self, recipe):
        cursor = self.getcursor()
        sql = "INSERT INTO recipes (name, meal_type, ingredients_count, ingredients_list, time, method) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            recipe.get("name"),
            recipe.get("meal_type"),
            recipe.get("ingredients_count"),
            recipe.get("ingredients_list"),
            recipe.get("time"),
            recipe.get("method")
        )
        cursor.execute(sql, values)
        self.connection.commit()
        recipe["id"] = cursor.lastrowid
        self.closeAll()
        return recipe

# update a recipe by id as a dict
    def update(self, id, recipe):
        cursor = self.getcursor()
        sql = """UPDATE recipes SET name=%s, meal_type=%s, ingredients_count=%s,
                 ingredients_list=%s, time=%s, method=%s WHERE id = %s"""
        values = (
            recipe.get("name"),
            recipe.get("meal_type"),
            recipe.get("ingredients_count"),
            recipe.get("ingredients_list"),
            recipe.get("time"),
            recipe.get("method"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {"message": "Recipe updated!"}
        

# delete a recipe by id. True or False

    def delete(self, id):
        cursor = self.getcursor()
        cursor.execute("DELETE FROM recipes WHERE id = %s", (id,))
        self.connection.commit()
        self.closeAll()
        return {"message": "Recipe deleted"}

# converts the raw database row into a dictionary so it can be returned as JSON
    def convertToDictionary(self, resultLine):
        keys = ['id', 'name', 'meal_type', 'ingredients_count', 'ingredients_list', 'time', 'method']
        return dict(zip(keys, resultLine))

        
recipe_dao = recipeDAO()