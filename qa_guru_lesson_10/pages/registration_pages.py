import os

from selene import browser as b, have, be


class RegistrationPage:
    def __init__(self):
        self.should_registered_user_with = b.element('.table').all('td').even

    def open_page(self):
        b.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        b.element('#firstName').should(be.blank).type(first_name)

    def fill_last_name(self, last_name):
        b.element('#lastName').should(be.blank).type(last_name)

    def fill_user_email(self, email):
        b.element('#userEmail').should(be.blank).type(email)

    def set_gender(self, gender):
        b.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_user_number(self, value):
        b.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, day, month, year):
        b.element('#dateOfBirthInput').click()
        b.element('.react-datepicker__year-select').type(year)
        b.element('.react-datepicker__month-select').type(month)
        b.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, value):
        b.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def set_hobbies(self, hobby):
        b.all('[for^= hobbies]').element_by(have.text(hobby)).element('..').click()

    def upload_picture(self, value):
        b.element('#uploadPicture').send_keys(os.path.abspath(f'picture/{value}'))

    def fill_current_address(self, address):
        b.element('#currentAddress').should(be.blank).type(address)

    def fill_state(self, value):
        b.element('#react-select-3-input').should(be.blank).type(value).press_enter()

    def fill_city(self, value):
        b.element('#react-select-4-input').should(be.blank).type(value).press_enter()

    def press_submit(self):
        b.element('#submit').click()

    def check_for_gratitude(self):
        b.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
