import time
import pytest
import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_001_Login:
    logger = LogGen.loggen()

    def test_successful_login(self):
        """Test successful login with valid credentials"""
        self.logger.info("********** Testing Successful Login **********")
        self.logger.info("Verifying login functionality with valid credentials...")

        self.lp = LoginPage(self.driver)
        try:
            self.lp.login(self.username, self.password)
            self.logger.info("Login method called with valid credentials.")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
            )
            self.logger.info("Dashboard loaded successfully. Login PASSED.")
            assert True

        except Exception as e:
            self._handle_test_failure("successful_login", e)
            assert False

    import allure  # ✅ Add this

    @allure.title("Login with Invalid Password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_password(self):
        self.logger.info("********** Testing Invalid Password Login **********")
        self.lp = LoginPage(self.driver)
        try:
            self.lp.login(self.username, "invalid_password")
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"))
            )
            assert "Invalid credentials" in error_message.text
            self.logger.info("Invalid password test PASSED")
        except Exception as e:
            self._handle_test_failure("invalid_password", e)
            assert False

    @allure.title("Login with Invalid Username")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_username(self):
        self.logger.info("********** Testing Invalid Username Login **********")
        self.lp = LoginPage(self.driver)
        try:
            self.lp.login("invalid@email.com", self.password)
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"))
            )
            assert "Invalid credentials" in error_message.text
            self.logger.info("Invalid username test PASSED")
        except Exception as e:
            self._handle_test_failure("invalid_username", e)
            assert False

    @allure.title("Login with Empty Credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_credentials(self):
        self.logger.info("********** Testing Empty Credentials Login **********")
        self.lp = LoginPage(self.driver)
        try:
            self.lp.login("", "")
            validation_messages = self.driver.find_elements(By.CLASS_NAME, "validation-message")
            assert len(validation_messages) > 0
            self.logger.info("Empty credentials validation test PASSED")
        except Exception as e:
            self._handle_test_failure("empty_credentials", e)
            assert False

    @allure.title("SQL Injection Attempt")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sql_injection_attempt(self):
        self.logger.info("********** Testing SQL Injection Prevention **********")
        self.lp = LoginPage(self.driver)
        try:
            sql_injection = "' OR '1'='1"
            self.lp.login(sql_injection, sql_injection)
            assert "dashboard" not in self.driver.current_url.lower()
            self.logger.info("SQL injection prevention test PASSED")
        except Exception as e:
            self._handle_test_failure("sql_injection", e)
            assert False

    def _handle_test_failure(self, test_name, exception):
        """Helper method to handle test failures"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")

        # Get the base directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the relative path to the Screenshots directory
        screenshot_dir = os.path.join(base_dir, "..", "Screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists

        # Full path for the screenshot file
        screenshot_path = os.path.join(screenshot_dir, f"test_{test_name}_failed_{timestamp}.png")

        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"Test {test_name} FAILED. Screenshot saved to: {screenshot_path}")
        self.logger.error(f"Exception: {str(exception)}")

        # ✅ Attach screenshot to Allure
        allure.attach.file(screenshot_path, name=f"{test_name}_screenshot", attachment_type=allure.attachment_type.PNG)