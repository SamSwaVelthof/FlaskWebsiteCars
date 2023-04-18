from flask import Blueprint,render_template,redirect,url_for
from showcar import db
from showcar.models import Car_Brand
from showcar.models import Car
from showcar.brands.forms import AddForm
from showcar.brands.forms import EditForm

car_brand_blueprint = Blueprint('brands', __name__, template_folder='templates')

@car_brand_blueprint.route("/")
def index():
    brands = Car_Brand.query.all()
    return render_template('brands/index.html', brands=brands)

@car_brand_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        brand = Car_Brand(
            name = form.name.data,
        )

        db.session.add(brand)
        db.session.commit()

        return redirect(url_for('brands.index'))
    return render_template('brands/add.html',form=form)

@car_brand_blueprint.route('/<string:slug>')
def single(slug):
    brand = Car_Brand.query.filter_by(slug=slug).first()
    cars = Car.query.filter_by(brand_id = brand.id).all()
    return render_template('brands/single.html', brand=brand, cars=cars)

@car_brand_blueprint.route('/edit/<string:slug>', methods=['GET', 'POST'])
def edit(slug):
    brand = Car_Brand.query.filter_by(slug=slug).first()
    form = EditForm()

    if form.validate_on_submit():
        brand.name = form.name.data
        db.session.commit()
        return redirect(url_for('brands.index'))
    else:
        form.name.data = brand.name

    return render_template('brands/edit.html', brand=brand, form=form)

@car_brand_blueprint.route('/delete/<int:id>')
def delete(id):
    brand = Car_Brand.query.filter_by(id=id).first()
    db.session.delete(brand)
    db.session.commit()

    return redirect(url_for('brands.index'))