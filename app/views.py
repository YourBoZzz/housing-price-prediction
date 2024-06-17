from flask import request, jsonify, render_template
from app import app, db
from app.models import HouseData
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Загрузка модели
model = xgb.XGBRegressor()
model.load_model('model/housing_model.json')

# Стандартный масштабировщик
scaler = StandardScaler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sqft_living = data['sqft_living']
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    floors = data['floors']
    year_built = data['year_built']
    condition = data['condition']
    latitude = data['latitude']
    longitude = data['longitude']

    # Подготовка данных для модели
    input_data = np.array([[sqft_living, bedrooms, bathrooms, floors, year_built, condition, latitude, longitude]])
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)[0]

    # Сохранение данных в базу данных
    house_data = HouseData(
        sqft_living=sqft_living,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        floors=floors,
        year_built=year_built,
        condition=condition,
        latitude=latitude,
        longitude=longitude,
        price=prediction
    )
    db.session.add(house_data)
    db.session.commit()

    return jsonify({'price': prediction})
