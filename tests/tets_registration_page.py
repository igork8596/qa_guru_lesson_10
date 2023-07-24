import os
from selene import browser as b, have, be, command
from faker import Faker

fake = Faker()


def test_registration_page():
    b.open('/automation-practice-form')
    first_name, last_name = [i for i in fake.name().split()]

    b.element('#firstName').should(be.blank).type(first_name)
    b.element('#lastName').should(be.blank).type(last_name)
    user_email = fake.email()
    b.element('#userEmail').should(be.blank).type(user_email)
    b.element('label[for="gender-radio-1"]').click()
    b.element('#userNumber').should(be.blank).type('9878763524')
    b.element('#dateOfBirthInput').click()
    b.element('[class="react-datepicker__month-select"]').click()
    b.element('[value="4"]').click()
    b.element('[class="react-datepicker__year-select"]').click()
    b.element('[value="1996"]').click()
    b.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    b.element('#subjectsInput').should(be.blank).type('Math').press_enter()
    for i in range(3):
        b.element(f'label[for="hobbies-checkbox-{i + 1}"]').click()
    b.element('#uploadPicture').send_keys(os.path.abspath('picture/Cat.jpeg'))
    b.element('#currentAddress').should(be.blank).type('996 William Rapid, New Gregoryton, UT 78395')
    b.element('#state').perform(command.js.scroll_into_view)
    b.element('#state').click()
    b.element('#react-select-3-option-1').click()
    b.element('#city').click()
    b.element('#react-select-4-option-1').click()
    b.element('#submit').perform(command.js.click)

    b.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    name = first_name + ' ' + last_name
    b.element('.table').all('td').even.should(
        have.exact_texts(
            name,
            user_email,
            'Male',
            '9878763524',
            '08 May,1996',
            'Maths',
            'Sports, Reading, Music',
            'Cat.jpeg',
            '996 William Rapid, New Gregoryton, UT 78395',
            'Uttar Pradesh Lucknow',
        )
    )
    b.element('#closeLargeModal').click()
