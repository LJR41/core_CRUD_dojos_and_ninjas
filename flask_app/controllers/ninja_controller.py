from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo
from flask_app import DATABASE

@app.route('/new/ninja')
def go_new_ninja():
    all_dojos = Dojo.display_dojo()
    return render_template('create_ninja.html', all_dojos=all_dojos)

@app.route('/create/ninja', methods=['POST'])
def create_new_ninja():
    Ninja.create_ninja(request.form)
    id = request.form['dojo_id']
    return redirect (f'/show/{id}/dojo')

