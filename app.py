from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet

app = Flask(__name__)
app.config["SECRET_KEY"] = '12345'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///petAdoption_db"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets = pets)


@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    form = AddPet()
    name=form.name.data
    species=form.species.data
    photo_url=form.photo_url.data
    age=form.age.data
    notes=form.notes.data
    available=form.available.data
    if form.validate_on_submit():
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age,notes=notes,available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')        
    else:
        return render_template('add-pet.html', form = form)


@app.route('/view-details/<int:pet_id>')
def view_details(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet-profile.html', pet = pet)

@app.route('/edit-pet/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    pet = Pet.query.get(pet_id)
    form = AddPet(obj=pet)
    name=form.name.data
    species=form.species.data
    photo_url=form.photo_url.data
    age=form.age.data
    notes=form.notes.data
    available=form.available.data
    if form.validate_on_submit():
        pet.name = name
        pet.species = species
        pet.photo_url = photo_url
        pet.age = age
        pet.notes = notes
        pet.available = available
        db.session.add(pet)
        db.session.commit()
        return redirect('/')  
    else:
        return render_template('edit-pet.html', form=form, pet=pet)
