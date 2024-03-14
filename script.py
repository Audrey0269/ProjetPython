from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)


#HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/cookingRecipes', methods=['GET'])
# def cooking_recipes_get():
#     name = "name" #request.form.get('name')
#     description = "descrciption" #request.form.get('description')
#     image = "image" #request.form.get('image')
#     return render_template('recipes.html')


#LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/login', methods=['POST', 'GET'])
# def login_post():

#     #Check if user exist in database
#     #user = User.query.filter_by(email=email).first()
#     #if not user:
#         #flash('Please ...')

#     #Retrive username and password from form
#     username = request.form.get('username')
#     password = request.form.get('password')
#     return redirect(url_for('recipes'))#, {escape(username)}



#REGISTRATION PAGE
@app.route('/registration')
def registration():
    return render_template('registration.html')

# @app.route('/registration', methods=['POST'])
# def registration_post():
#     #Retrive values from form
#     username = "username" #request.form.get('username')
#     password = "password" #request.form.get('password')
#     email = "email@email.fr" #request.form.get('email')
#     return redirect(url_for('login'))#, {escape(username)}







 





#CREATE RECIPE PAGE
@app.route('/createRecipe')
def create_recipe():
    return render_template('createRecipe.html')

# @app.route('/create_cooking_recipes', methods=['POST'])
# def cooking_recipes_post():
#     name = "name" #request.form.get('name')
#     description = "descrciption" #request.form.get('description')
#     image = "image" #request.form.get('image')
#     return redirect(url_for('recipes'))#, {escape(username)}


#RECIPE PAGE
@app.route('/recipe')
def recipe():
    return render_template('recipe.html')
                    


#LOGOUT PAGE
@app.route('/logout')
def logout():
    return redirect(url_for('login'))





