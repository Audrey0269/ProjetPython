from flask import Flask, render_template
from flask import url_for
from markupsafe import escape
from flask import request


app = Flask(__name__)



#HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')

#RECIPE PAGE
@app.route('/recipes') #/<int:id>')
def recipes(): #mettre (id) entre les parenthèses
    return render_template('recipes.html') #mettre apres : html', id=id)


#LOGIN PAGE
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)



#LOGOUT PAGE
@app.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html') #ou : return redirect(url.for('index'))





#mettre le truc quand connexion =sécurité

