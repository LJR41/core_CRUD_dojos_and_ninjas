from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja
from flask_app import DATABASE

@app.route('/')
def display_all_dojo():
    all_dojos = Dojo.display_dojo()
    return render_template('dojos.html', all_dojos=all_dojos)

@app.route('/new/dojo')
def go_new_dojo():
    return render_template('create_dojo.html')

@app.route('/create/dojo', methods=['POST'])
def create_new_dojo():
    id = Dojo.create_dojo(request.form)
    return redirect(f'/show/{id}/dojo')

@app.route('/show/<int:id>/dojo')
def show_dojo(id):
    data = {
        'id' : id
    }
    all_ninjas = Ninja.ninjas_in_dojo(data)
    print(all_ninjas)
    one_dojo = Dojo.show_dojo(data)
    return render_template('show_one_dojo.html', one_dojo=one_dojo,all_ninjas=all_ninjas)
