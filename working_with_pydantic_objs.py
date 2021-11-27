from app import Gender, Person


if __name__ == '__main__':
    person = Person(
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
    print(person)
    person_dict = person.dict()
    print(person_dict)
    print(person_dict["address"]["city"])
    person_include = person.dict(include={"first_name", "last_name"})
    print(person_include)

    person_exclude = person.dict(exclude={"interests", "birthdate"})
    print(person_exclude)

    person_nested_include = person.dict(include={
        "first_name": ...,
        "last_name": ...,
        "address": {"street", "city"}
    })
    print(person_nested_include)

    user_dict = person.user_dict()
    print(user_dict)
