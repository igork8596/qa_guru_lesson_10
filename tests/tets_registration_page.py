from models.user import User
from qa_guru_lesson_10.pages.registration_pages import RegistrationPage
from qa_guru_lesson_10.resource import first_name, last_name, user_email


def test_registration_user():
    registration_page = RegistrationPage()

    test_user = User(
        first_name=first_name,
        last_name=last_name,
        email=user_email,
        gender='Male',
        phone_number='98787675641',
        date_of_birth=('08', 'May', '1996'),
        subjects='Maths',
        hobbies='Sports',
        picture='Cat.jpeg',
        current_address='996 William Rapid, New Gregoryton, UT 78395',
        state='Uttar Pradesh',
        city='Lucknow'
    )

    registration_page.open_page()
    registration_page.register_user(test_user)
    registration_page.sshould_have_registered(test_user)
