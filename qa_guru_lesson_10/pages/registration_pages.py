import os

from selene import browser as b, have, be
from models.user import User
from qa_guru_lesson_10.resource import full_name, user_email


class RegistrationPage:
    def __init__(self):
        self.first_name = b.element('#firstName')
        self.last_name = b.element('#lastName')
        self.email = b.element('#userEmail')
        self.gender = b.all('[name=gender]')
        self.phone_number = b.element('#userNumber')
        self.subjects = b.element('#subjectsInput')
        self.hobbies = b.all('[for^= hobbies]')
        self.upload_picture = b.element('#uploadPicture')
        self.current_address = b.element('#currentAddress')

    def open_page(self):
        b.open('/automation-practice-form')

    def register_user(self, user: User):
        self.first_name.should(be.blank).type(user.first_name)
        self.last_name.should(be.blank).type(user.last_name)
        self.email.should(be.blank).type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.phone_number.should(be.blank).type(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth[0], user.date_of_birth[1], user.date_of_birth[2])
        self.subjects.should(be.blank).type(user.subjects).press_enter()
        self.hobbies.element_by(have.text(user.hobbies)).element('..').click()
        self.upload_picture.send_keys(os.path.abspath(f'picture/{user.picture}'))
        self.current_address.should(be.blank).type(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.press_submit()

    def fill_date_of_birth(self, day, month, year):
        b.element('#dateOfBirthInput').click()
        b.element('.react-datepicker__year-select').type(year)
        b.element('.react-datepicker__month-select').type(month)
        b.element(f'.react-datepicker__day--0{day}').click()

    def fill_state(self, value):
        b.element('#react-select-3-input').should(be.blank).type(value).press_enter()

    def fill_city(self, value):
        b.element('#react-select-4-input').should(be.blank).type(value).press_enter()

    def press_submit(self):
        b.element('#submit').click()

    def sshould_have_registered(self, user: User):
        b.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        b.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user_email,
                'Male',
                '9878767564',
                '08 May,1996',
                'Maths',
                'Sports',
                'Cat.jpeg',
                '996 William Rapid, New Gregoryton, UT 78395',
                'Uttar Pradesh Lucknow'
            )
        )
