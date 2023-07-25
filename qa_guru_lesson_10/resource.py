from faker import Faker

fake = Faker()
first_name, last_name = [i for i in fake.name().split()]
user_email = fake.email()
full_name = first_name + ' ' + last_name
