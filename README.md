# Car-Price-Predictor-With-FastApi-
This project will predict the price of cars and Expose a FastApi for it so that external world can predict the price with the help of Api and Will be useable in Web apps, Mobile apps, Desktop Apps.

**The requirements for webapi**
```python
pip install fastapi

# Define routes
@app.post('/predict')
def car_price_predictor(data: Car):
    car_dict = data.dict()
    price = pipe.predict(
        pd.DataFrame(
            columns=['name','company','year','kms_driven','fuel_type'],
            data=np.array([car_dict.get("name"),car_dict.get('company'),
            car_dict.get('year'),car_dict.get('kms_driven'),car_dict.get('fuel_type')]).reshape(1,5)
        )
    )
    return {"price": price}

pip install pydantic

class Car(BaseModel):
    name : str
    company : str
    year : int
    kms_driven : int
    fuel_type : str

```

We have designed a wep api with the help of FastApi You can check it out in code.
