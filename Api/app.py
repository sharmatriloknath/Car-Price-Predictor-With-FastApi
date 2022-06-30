from fastapi import FastAPI
import uvicorn
from car import Car
import pandas as pd
import numpy as np

import pickle


# app initialization
app = FastAPI()


# get pipe
pipe = pickle.load(open('../Model/pipe.pkl','rb'))


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




if __name__ == '__main__':
    uvicorn.run(app=app, debug=True)

# uvicorn app:app --reload