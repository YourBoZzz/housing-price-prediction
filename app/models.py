from app import db

class HouseData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sqft_living = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)
    floors = db.Column(db.Integer, nullable=False)
    year_built = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<HouseData {self.id}>'
