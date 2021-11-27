from pydantic import BaseModel, ValidationError, Field, EmailStr, HttpUrl
from typing import List, Optional
from datetime import date
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"


class Address(BaseModel):
    street: str
    postal_code: int
    city: str
    country: str


class Person(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=255)
    last_name: str = Field(..., min_length=3, max_length=255)
    age: int = Field(..., ge=0, le=120)
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Optional[Address]

    def user_dict(self):
        return self.dict(include={"first_name", "last_name", "age", "gender"})


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


if __name__ == '__main__':
    try:
        john = Person(
            first_name="John",
            last_name="Doe",
            age=25,
            gender=Gender.MALE,
            birthdate="1996-03-06",
            interests=["Football", "Heavy Metal", "Code"],
            address={
                "street": "123 Imaginary Street",
                "postal_code": 12345,
                "city": "Imaginary City",
                "country": "Wonderland",

            }
        )
        print(john)

    except ValidationError as ve:
        print(str(ve))

    try:
        user = User(email="a@g.com", website="https://s.com")
        print(user)
    except ValidationError as ve:
        print(str(ve))

