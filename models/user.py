import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: tuple
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str
