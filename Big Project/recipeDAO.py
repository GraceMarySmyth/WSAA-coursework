import mysql.connector
import dbconfig as cfg
class recipeDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from recipes"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from recipes where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, recipe):
        cursor = self.getcursor()
        sql="insert into recipes (name, meal_type, ingredients_count, ingredients_list, time, method) values (%s,%s,%s)"
        values = (book.get("name"), book.get("meal_type"), book.get("ingredients_count"), book.get("ingredients_list"), book.get("time"), book.get("method"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        recipe["id"] = newid
        self.closeAll()
        return recipe


    def update(self, id, recipes):
        cursor = self.getcursor()
        sql="update recipes set name= %s, meal_type=%s, ingredient_count=%s, ingredient_list=%s, time=%s, method=%s  where id = %s"
        values = (recipes.get("name"), recipes.get("meal_type"), recipes.get("ingredients_count"), recipes.get("ingredients_list"), recipes.get("time"), recipes.get("method"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from recipes where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['id','name','meal_type', "ingredients_count", "ingredients_list", "time", "method"]
        book = {}
        currentkey = 0
        for attrib in resultLine:
            book[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return book

        
recipeDAO = recipeDAO()