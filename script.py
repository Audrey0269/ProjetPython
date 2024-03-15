from flask import Flask, render_template, redirect, url_for, request, g
from pathlib import Path
from werkzeug.utils import secure_filename

import sqlite3
import os

app = Flask(__name__)

#Path where image will save
UPLOAD_FOLDER = 'static/images'

#formats accepted
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


#______________________________DATABASE______________________________

DATABASE = "database.db"

# CONNECTION TO DATABASE (create empty database)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# CLOSE DATABASE
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


#_______________________________APP___________________________

#HOME PAGE
@app.route('/')
def home():
    #Recover username from URL 
    username = request.args.get('username')

    #if username in URL
    if username:
        welcome_message = f'Bonjour {username} !'
    else:
        welcome_message = 'Bienvenu sur le site CookingRecipes'

    #Create cursor to database
    cur = get_db().cursor()

    #Request to have all recipes
    cur.execute('SELECT * FROM recipes;')

    #Recover all recipes
    recipes = cur.fetchall()

    #close cursor
    cur.close()

    return render_template('home.html', recipes=recipes, welcome_message=welcome_message)


#LOGIN PAGE
@app.route('/login', methods=['POST', 'GET'])
def login_post():

    #Initialize variable error_message to None
    error_message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #Create cursor to database
        cur = get_db().cursor()

        #Check if username and password are in database
        cur.execute('SELECT * FROM users WHERE username = ? AND password = ?' , (username, password))
        user = cur.fetchone()
        cur.close()

        #if username and password are in database
        if user:
            return redirect(url_for('home', username=username))
        #if they aren't in database
        else:
            error_message = "Invalid username or password."

    return render_template('login.html', error_message=error_message)


#REGISTRATION PAGE
@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def registration_post():
   
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    #Create cursor to database
    cur = get_db().cursor()

    #Request to have all recipes
    cur.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
    get_db().commit()

    #close cursor
    cur.close()

    return redirect(url_for('login_post'))#, {escape(username)}


#CREATE RECIPE PAGE
@app.route('/createRecipe')
def create_recipe():
    return render_template('createRecipe.html')


@app.route('/create_cooking_recipes', methods=['POST'])
def cooking_recipes_post():

    name = request.form.get('name')
    description = request.form.get('description')
    image = request.files['image']

    #Secure file names
    filename = secure_filename(image.filename)

    # Save image
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    #Path to image
    image_path = os.path.join('', filename)

    #Add recipe to database with image path
    cur = get_db().cursor()
    cur.execute('INSERT INTO recipes (name, description, image) VALUES (?, ?, ?)', (name, description, image_path))
    get_db().commit()
    cur.close()

    return redirect(url_for('home'))


#DETAIL RECIPE PAGE
@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):

    #Create cursor to database
    cur = get_db().cursor()

    #Request to have all recipes
    cur.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))

    #Select recipe
    recipe = cur.fetchone()

    #close cursor
    cur.close()

    return render_template('recipeDetail.html', recipe=recipe)
                    


#LOGOUT PAGE
@app.route('/logout')
def logout():
    return redirect(url_for('login_post'))


#__________________________DATABASE__________________________

# IF DATABASE NOT EXIST
if not Path('database.db').exists():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()