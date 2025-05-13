from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen  # ✅ Import your logger


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()  # ✅ Initialize logger

        self.username_field = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
        self.password_field = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        self.loginBtn = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.error_message = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")

    def enter_username(self, username):
        self.logger.info(f"Entering username: {username}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        self.logger.info("Entering password.")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login_btn(self):
        self.logger.info("Clicking login button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.loginBtn)
        ).click()

    def get_error_message(self):
        self.logger.warning("Fetching error message.")
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.error_message)
        ).text

    def login(self, username="Admin", password="admin123"):
        self.logger.info("Performing login operation.")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
            )
            self.logger.info("Login successful and dashboard loaded.")
        except:
            self.logger.error("Login failed. Capturing screenshot.")
            self.driver.save_screenshot("login_failed.png")
            raise Exception("Login failed or dashboard not loaded.")