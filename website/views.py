from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .components.dropdownDogBreedInfo import get_dropdown_menu
from .models import Note, Dogs, Trainer

import random




training_types = [
    "Obedience Training",
    "Therapy Training",
    "Behavioral Training",
    "Agility Training",
    "Protection Training",
    "Service Training",
    "Tracking Training"
]

sizes = [
    {"value": "small", "text": "Less than 22lbs"},
    {"value": "medium", "text": "22 - 57lbs"},
    {"value": "large", "text": "Greater than 57lbs"}
]

experiences = [
    {"value": "less_than_5", "text": "Less than 5 years"},
    {"value": "5_to_10", "text": "5 - 10 years"},
    {"value": "10_plus", "text": "10+ years"}
]

cities = [
    "Seattle",
    "Spokane",
    "Tacoma",
    "Bellevue",
    "Kent",
    "Everett"
]

# Function to generate 50 fake dog trainer data objects
def generate_fake_trainers():
    from .models import Trainer # Importing Trainer model here to avoid circular import
 
    fake_trainers = []
    for _ in range(50):
        name = f"Fake Trainer {_}"
        training_type = random.choice(training_types)
        size = random.choice(sizes)["value"]  # Extract the value from the size dictionary
        experience = random.choice(experiences)["value"]  # Extract the value from the experience dictionary
        city = random.choice(cities)

        trainer = Trainer(name=name, training_type=training_type, size=size, experience=experience, city=city)
        fake_trainers.append(trainer)

    # Add the fake trainers to the database and commit the changes
    db.session.bulk_save_objects(fake_trainers)
    db.session.commit()

    return fake_trainers

def fetch_filtered_trainers(training_type, size, experience, city):
    # Build a filter query based on the selected criteria
    filter_query = Trainer.query.filter(
        (Trainer.training_type == training_type if training_type else True) &
        (Trainer.size == size if size else True) &
        (Trainer.experience == experience if experience else True) &
        (Trainer.city == city if city else True)
    )
    return filter_query.all()





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




#######

@views.route('/search-trainer', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        # Get the selected criteria from the form submission
        training_type = request.form.get('training_type')
        size = request.form.get('size')
        experience = request.form.get('experience')
        city = request.form.get('city')
    else:
        # If it's an initial GET request, use the query parameters from the URL
        training_type = request.args.get('training_type')
        size = request.args.get('size')
        experience = request.args.get('experience')
        city = request.args.get('city')

    # Fetch the filtered trainers based on the selected filters
    filtered_trainers = fetch_filtered_trainers(training_type, size, experience, city)

    return render_template(
        "searchTrainer.html",
        filtered_trainers=filtered_trainers,
        training_types=training_types,
        sizes=sizes,
        experiences=experiences,
        cities=cities,
        selected_training_type=training_type,  # Pass the selected filter options to pre-select the dropdowns
        selected_size=size,
        selected_experience=experience,
        selected_city=city,
        user=current_user
    )
