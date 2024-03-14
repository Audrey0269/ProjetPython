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
    #Create cursor to database
    cur = get_db().cursor()
    #Request to have all recipes
    cur.execute('SELECT * FROM recipes;')
    #Recover all recipes
    recipes = cur.fetchall()
    #close cursor
    cur.close()
    return render_template('home.html', recipes=recipes)


#LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login_post():

   
     #Check if user exist in database
    username = request.form.get('username')
    print(username)

    password = request.form.get('password')
    print(password)

    # cur = get_db().cursor()
    # cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    # user = cur.fetchone() 

    # if user is None:
    #     raise ValueError("Identifiants invalides. Veuillez vérifier votre nom d'utilisateur et votre mot de passe.")

    # if username != 'Audrey' and password !='123456':
    #     error_username = "Nom d'utilisateur incorrect."
        #raise ValueError("Identifiants invalides. Veuillez vérifier votre nom d'utilisateur et votre mot de passe.")
    
    return redirect(url_for('home'))#, {escape(username)}

#pour page de connexion faire : requete SELECT quand user = et password = 
#bien faire commit à chaque modification de la BDD 


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

    return redirect(url_for('login'))#, {escape(username)}


#CREATE RECIPE PAGE
@app.route('/createRecipe')
def create_recipe():
    return render_template('createRecipe.html')

@app.route('/create_cooking_recipes', methods=['POST'])
def cooking_recipes_post():

    name = request.form.get('name')
    description = request.form.get('description')
    image = request.form.get('image')

    #Create cursor to database
    cur = get_db().cursor()
    #Request to have all recipes
    cur.execute('INSERT INTO recipes (name, description, image) VALUES (?, ?, ?)', (name, description, image))
    get_db().commit()
    #close cursor
    cur.close()

    return redirect(url_for('home'))    #, {escape(username)}





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