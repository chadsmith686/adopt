from forms import AddPetForm, EditPetForm
from flask import Flask, request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pet_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

# toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def list_all_pets():
    """List all pets."""
    
    pets = Pet.query.all()
    return render_template('all_pets.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """"Shows form to add a pet to database."""
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            available = form.available.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
        
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>')
def edit_pet(pet_id):
    """Edit Pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
    return render_template('edit_pet.html', pet=pet, form=form)