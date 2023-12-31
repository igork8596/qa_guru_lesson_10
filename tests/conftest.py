import pytest
from selene import browser as b
from os import path as p


@pytest.fixture(scope='function', autouse=False)
def way_to_dir():
    return p.dirname(__file__)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    b.config.base_url = 'https://demoqa.com'
    b.config.window_width = 1440
    b.config.window_height = 2160

    yield

    b.quit()
