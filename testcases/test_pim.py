import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.PimPage import Pim
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_003_Pim:
    logger = LogGen.loggen()

    def setup_method(self):
        config = ReadConfig()
        self.base_url = config.getApplicationURL()
        self.username = config.getUsername()
        self.password = config.getPassword()
        self.fn = "Manoj"
        self.mn = "Kumar"
        self.ln = "Sharma"
        self.id = "1234"

    def test_pimuser(self):
        self.logger.info("========== Test_003_Pim STARTED ==========")
        self.driver.get(self.base_url)
        self.logger.info(f"Navigated to {self.base_url}")

        self.pm = Pim(self.driver)
        self.logger.info("Performing login...")

        self.pm.enterUserName(self.username)
        self.pm.setPassword(self.password)
        self.pm.clickLogin()

        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        self.logger.info("Login successful. On Dashboard.")

        self.logger.info("Navigating to PIM module to add user...")
        self.pm.clickpimbutton()
        self.pm.clickaddbutton()
        self.pm.addfirstname(self.fn)
        self.pm.addmiddlename(self.mn)
        self.pm.addlastname(self.ln)
        self.pm.addemployeeid(self.id)
        self.pm.clicksavebutton()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
            )
            assert "personalDetails" in self.driver.current_url or "viewPersonalDetails" in self.driver.current_url
            self.logger.info("✅ Employee added successfully. Redirected to Personal Details page.")
        except Exception as e:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"/Users/vivekkumar/screenshots/test_pim_failed_{timestamp}.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"❌ Failed to add employee or redirect. Screenshot saved: {screenshot_path}")
            self.logger.error(f"Exception: {str(e)}")
            assert False

        self.logger.info("========== Test_003_Pim COMPLETED ==========")