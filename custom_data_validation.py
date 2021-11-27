from pydantic import validator, BaseModel, EmailStr, root_validator
from datetime import date


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    # validation at field level
    @validator("birthdate")
    def validate_birthdate(cls, value: date):
        delta = date.today() - value
        age = delta.days / 365
        if age > 120:
            raise ValueError("You are too old.")
        return value


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirm: str

    @root_validator
    def validate_password(cls, values):
        password = values.get("password")
        password_confirm = values.get("password_confirm")

        if password != password_confirm:
            raise ValueError("Password do not match.")
        return values


if __name__ == '__main__':
    person = Person(first_name="Sam", last_name="walter", birthdate="1997-03-06")
    print(person)
    user = UserRegistration(email="s@g.com", password="123", password_confirm="1234")
    print(user)
