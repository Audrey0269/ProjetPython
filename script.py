from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

#LOGIN PAGE
@app.route('/')
def login():
        return render_template('home.html')


@app.route('/', methods=['POST'])
def login_post():

    #Check if user exist in database
    #user = User.query.filter_by(email=email).first()
    #if not user:
        #flash('Please ...')

    #Retrive username and password from form
    username = "username" #request.form.get('username')
    password = "password" #request.form.get('password')
    return redirect(url_for('recipes'))#, {escape(username)}



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





 
#RECIPES PAGE
@app.route('/cooking_recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/cooking_recipes', methods=['GET'])
def cooking_recipes_get():
    name = "name" #request.form.get('name')
    description = "descrciption" #request.form.get('description')
    image = "image" #request.form.get('image')
    return render_template('recipes.html')




#CREATE RECIPE PAGE
@app.route('/create_cooking_recipes')
def create_recipes():
    return render_template('createRecipe.html')

@app.route('/create_cooking_recipes', methods=['POST'])
def cooking_recipes_post():
    name = "name" #request.form.get('name')
    description = "descrciption" #request.form.get('description')
    image = "image" #request.form.get('image')
    return redirect(url_for('recipes'))#, {escape(username)}



#LOGOUT PAGE
@app.route('/logout')
def logout():
    return redirect(url_for('login'))


