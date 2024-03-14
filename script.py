from flask import Flask, render_template, redirect, url_for, request, g
from markupsafe import escape
from pathlib import Path

import sqlite3

app = Flask(__name__)


#______________________________DATABASE______________________________
DATABASE = "database.db"

# CONNEXION TO DATABASE (create empty database)
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
    #Create cursur to SQL
    cur = get_db().cursor()
    cur.execute('SELECT * FROM recipes')




    # for user in query_db('select * from users'):
    # print(user['username'], 'has the id', user['user_id'])

     # rv = cur.fetchall()
    # cur.close()

    return render_template('home.html')



#SELECT*FROM TABLE

#LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login_post():
    cur = get_db().cursor()
    cur.execute('SELECT username FROM users WHERE =')


    #Check if user exist in database
    username = request.form.get('username')
    password = request.form.get('password')
    if username != "Audrey" and password !=123456:
        return "invalid ID or MDP !"
    
    return redirect(url_for('home'))#, {escape(username)}

#pour page de connexion faire : requete SELECT quand user = et password = 
#bien faire commit à chaque modification de la BDD 


#REGISTRATION PAGE
@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def registration_post():
    #Retrive values from form
    username = "username" #request.form.get('username')
    password = "password" #request.form.get('password')
    email = "email@email.fr" #request.form.get('email')
    return redirect(url_for('login'))#, {escape(username)}


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



#__________________________DATABASE__________________________

# IF DATABASE NOT EXIST
if not Path('database.db').exists():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()




# Pour lire le fichier SQL
# Path('schema.sql').read_text()