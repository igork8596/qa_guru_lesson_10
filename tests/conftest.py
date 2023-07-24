import pytest
from selene import browser as b


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    b.config.base_url = 'https://demoqa.com'
    b.config.window_width = 1440
    b.config.window_height = 2160

    yield

    b.quit()
