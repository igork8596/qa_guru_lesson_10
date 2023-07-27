from selene import have
from qa_guru_lesson_10.pages.registration_pages import RegistrationPage
from qa_guru_lesson_10.resource import first_name, last_name, user_email, full_name


def test_registration_page():
    registration_page = RegistrationPage()
    registration_page.open_page()

    registration_page.fill_first_name(first_name=first_name)
    registration_page.fill_last_name(last_name=last_name)
    registration_page.fill_user_email(email=user_email)
    registration_page.set_gender(gender='Male')
    registration_page.fill_user_number(value='9878767564')
    registration_page.fill_date_of_birth('08', 'May', '1996')
    registration_page.fill_subjects(value='Maths')
    registration_page.set_hobbies(hobby='Sports')
    registration_page.upload_picture('Cat.jpeg')
    registration_page.fill_current_address('996 William Rapid, New Gregoryton, UT 78395')
    registration_page.fill_state(value='Uttar Pradesh')
    registration_page.fill_city(value='Lucknow')

    registration_page.press_submit()

    registration_page.check_for_gratitude()
    registration_page.should_registered_user_with.should(
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
