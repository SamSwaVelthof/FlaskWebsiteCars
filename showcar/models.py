from showcar import db
from slugify import slugify

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    brand_id = db.Column(db.Integer, db.ForeignKey('car_brand.id'), nullable = False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255))
    page_content = db.Column(db.String())

    # Create a slug bases on the name of the car
    @staticmethod
    def slugify(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

db.event.listen(Car.name, 'set', Car.slugify, retval=False)

class Car_Brand(db.Model):
    __tablename__ = 'car_brand'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(255))

    # Create a slug bases on the name of the brand
    @staticmethod
    def slugify(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

db.event.listen(Car_Brand.name, 'set', Car_Brand.slugify, retval=False)



