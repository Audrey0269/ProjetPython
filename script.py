from flask import Flask, render_template, redirect
from flask import url_for
from markupsafe import escape
from flask import request

app = Flask(__name__)


#LOGIN PAGE
@app.route('/')
def login():
        return render_template('home.html')

@app.route('/', methods=['POST'])
def login_post():
    username = "username" #request.form.get('username')
    password = "password" #request.form.get('password')
    return redirect(url_for('recipes'))

#REGISTRATION PAGE
@app.route('/registration')
def registration():
        return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def registration_post():
    username = "username" #request.form.get('username')
    password = "password" #request.form.get('password')
    email = "email" #request.form.get('email')
    return redirect(url_for('login'))





 
#RECIPES PAGE
@app.route('/cooking_recipes')
def recipes():
    return render_template('recipes.html')


#CREATE RECIPE PAGE
@app.route('/create_cooking_recipes')
def recipes():
    return render_template('recipes.html')



#LOGOUT PAGE
@app.route('/logout')
def logout():
    return redirect(url_for('login'))






#RECIPE PAGE
# @app.route('/recipe') #/<int:id>')
# def recipes(): #mettre (id) entre les parenthèses
#     return render_template('recipes.html') #mettre apres : html', id=id)

#mettre le truc quand connexion =sécurité

