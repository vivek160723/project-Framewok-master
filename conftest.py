import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    config_reader = ReadConfig()
    base_url = config_reader.getApplicationURL()
    username = config_reader.getUsername()
    password = config_reader.getPassword()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    driver.get(base_url)
    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    yield
    driver.quit()