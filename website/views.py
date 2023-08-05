from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from .models import Dogs
from . import db
import json
from .components.dropdownDogBreedInfo import get_dropdown_menu


# Blueprint helps split and organize our view file.
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 
        
        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')
        
        # Redirect the user to another route (e.g., /notes) after successful POST
        return redirect(url_for('views.home'))
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("home.html", notes=notes, user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():  

    note = json.loads(request.data) # grabs the string as JSON from the INDEX.js file and turns it into python dictionary object
    noteId = note['noteId'] # Then we can access the noteId.
    note = Note.query.get(noteId)

    if note and note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            print("note deleted successfully")
            flash('Note deleted!', category='success')
    return jsonify({}) 


@views.route('/delete-dog', methods=['POST'])
@login_required
def delete_dog():  

    dog = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    dogID = dog['dogID']
    dog = Dogs.query.get(dogID)

    if dog and dog.user_id == current_user.id:
            db.session.delete(dog)
            db.session.commit()
            flash('dog deleted!', category='success')
    return jsonify({})



@views.route('/training', methods=['GET', 'POST'])
@login_required
def training():

    if request.method == 'POST':
        dog_name = request.form.get('dog_name')
        dog_image = request.form.get('dog_image')

        if len(dog_name) < 1:
            flash('Dog name must be greater than 1 character.', category='error')

        elif len(dog_name) > 12:
            flash('Dog name must be less than 12 characters', category='error')

        elif not dog_image:
            flash('You must pick a dog breed.', category='error')

        else:
        # Save the selected dog information to the logged-in user
            new_dog_info = Dogs(dog_name=dog_name, dog_image=dog_image, user_id=current_user.id)
            db.session.add(new_dog_info)
            db.session.commit()
            flash('Dog registration successful!', category='success')
            return redirect(url_for('views.training'))
        
    dogs = Dogs.query.filter_by(user_id=current_user.id).all()

    return render_template("training.html", user=current_user, get_dropdown_menu=get_dropdown_menu, dogs=dogs)


@views.route('/about', methods=['GET', 'POST'])
def about():
    
    return render_template("about.html", user=current_user)
