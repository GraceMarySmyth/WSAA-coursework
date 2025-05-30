from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Time
from sqlalchemy.sql import text
from recipeDAO import recipe_dao
from flask_cors import CORS



# Imports to support users downloading the recipes as either a CSV or JSON file
import csv
import io
from flask import make_response

# Create a Flask application instance
# This is the main entry point for the application
app = Flask("Smyth_Family_Recipes")
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/smyth_family_recipes'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__ = 'recipes'
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
            "time": str(self.time),
            "method": self.method
        }
    
#mapping the root URL to a function
# This function will be called when the root URL is accessed
#@app.route('/')
#def index():
#    return "<h1>Welcome to the Smyth Family Recipe API!</h1>"

@app.route('/')
def home():
    return render_template("recipe_viewer.html")

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

# Export recipes as JSON or CSV
@app.route("/recipes/export/<string:format>", methods=["GET"])
def export_recipes(format):
    recipes = recipe_dao.getAll()

    if format == "json":
        return jsonify(recipes)

    elif format == "csv":
        # Create in-memory CSV
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=recipes[0].keys())
        writer.writeheader()
        writer.writerows(recipes)
        output.seek(0)

        # Send as CSV download
        response = make_response(output.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=recipes.csv"
        response.headers["Content-type"] = "text/csv"
        return response

    else:
        return jsonify({"error": "Unsupported export format. Use 'json' or 'csv'."}), 400

# commented out to get python anywhere to work and replaced with below
  #  if __name__ == "__main__":
  #      with app.app_context():
  #          db.create_all()
#     app.run(debug = True)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()