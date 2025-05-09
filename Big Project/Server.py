from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("Smyth_Family_Recipes")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    meal_type = db.Column(db.String(50))
    ingredients_count = db.Column(db.Integer)
    ingredients_list = db.Column(db.Text)
    time = db.Column(db.String(50))
    method = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "meal_type": self.meal_type,
            "ingredients_count": self.ingredients_count,
            "ingredients_list": self.ingredients_list,
            "time": self.time,
            "method": self.method
        }
    

@app.route('/')
def index():
    return "Welcome to the Smyth Family Recipe API!"

#get all recipes
@app.route("/recipes", methods=["GET"])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

#GET one recipe
@app.route("/recipes/<int:id>", methods=["GET"])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    return jsonify(recipe.to_dict())

#add a recipe/POST a recipe
@app.route("/recipes", methods=["POST"])
def add_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        name=data["name"],
        meal_type=data["meal_type"],
        ingredients_count=data["ingredients_count"],
        ingredients_list=data["ingredients_list"],
        time=data["time"],
        method=data["method"]
    )
    db.session.add(new_recipe)
    db.session.commit() # This will save the new recipe to the database
    return jsonify(new_recipe.to_dict()), 201

# PUT update existing recipe
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.get_json()
    recipe.name = data['name']
    recipe.meal_type = data['meal_type']
    recipe.ingredients_count = data['ingredients_count']
    recipe.time = data['time']
    recipe.method = data['method']
    db.session.commit()
    return jsonify(recipe.to_dict())

# DELETE a recipe
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted"})


if __name__ == "__main__":
   with app.app_context():
        db.create_all()   
    app.run(debug = True)