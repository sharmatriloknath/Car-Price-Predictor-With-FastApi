from pydantic import BaseModel


class Car(BaseModel):
    name : str
    company : str
    year : int
    kms_driven : int
    fuel_type : str