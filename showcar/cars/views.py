from flask import Blueprint,render_template,redirect,url_for
from showcar import db
from showcar.models import Car
from showcar.models import Car_Brand
from showcar.cars.forms import AddForm
from showcar.cars.forms import EditForm

car_blueprint = Blueprint('cars', __name__, template_folder='templates')

@car_blueprint.route("/")
def index():
    cars = Car.query.all()
    
    return render_template('cars/index.html', cars=cars)

@car_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    form.brand.choices = [(Car_Brand.id, Car_Brand.name) for Car_Brand in Car_Brand.query.all()]

    if form.validate_on_submit():
        car = Car(
            name = form.name.data,
            description = form.description.data,

            # TODO: add relations later
            user_id = 1,
            brand_id = form.brand.data,
        )

        db.session.add(car)
        db.session.commit()

        return redirect(url_for('cars.index'))
    return render_template('cars/add.html',form=form)

@car_blueprint.route('/<string:slug>')
def single(slug):
    car = Car.query.filter_by(slug = slug).first()
    brand = Car_Brand.query.filter_by(id = car.brand_id).first()
    related_cars = Car.query.filter_by(brand_id = brand.id).filter(id != car.id).all()
    
    return render_template('cars/single.html', car=car, brand=brand, related_cars=related_cars)

@car_blueprint.route('/edit/<string:slug>', methods=['GET', 'POST'])
def edit(slug):
    car = Car.query.filter_by(slug=slug).first()
    form = EditForm()
    form.brand.choices = [(Car_Brand.id, Car_Brand.name) for Car_Brand in Car_Brand.query.all()]

    if form.validate_on_submit():
        car.name = form.name.data
        car.description = form.description.data
        car.brand_id = form.brand.data
        
        db.session.commit()

        return redirect(url_for('cars.index'))
    else:
        form.name.data = car.name
        form.description.data = car.description

    return render_template('cars/edit.html', car=car, form=form)

@car_blueprint.route('/delete/<int:id>')
def delete(id):
    car = Car.query.filter_by(id=id).first()
    db.session.delete(car)
    db.session.commit()

    return redirect(url_for('cars.index'))

    
