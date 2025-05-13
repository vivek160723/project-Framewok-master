import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.SearchPage import Search
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_004_Search:
    def setup_method(self):
        config = ReadConfig()
        self.base_url = config.getApplicationURL()
        self.username = config.getUsername()
        self.password = config.getPassword()
        self.si = "PIM"
        self.logger = LogGen.loggen()

    def test_search(self):
        self.logger.info("====== Starting Test_004_Search ======")
        self.driver.get(self.base_url)
        self.logger.info(f"Opened URL: {self.base_url}")

        self.s = Search(self.driver)

        self.logger.info("Entering login credentials...")
        self.s.enterUserName(self.username)
        self.s.setPassword(self.password)
        self.s.clickLogin()

        # Wait until dashboard is loaded
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )
        self.logger.info("Login successful. On dashboard page.")

        self.logger.info("Performing search operation...")
        self.s.clicksearchbutton()
        self.s.addsearchitem(self.si)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//span[text()='{self.si}']"))
            )
            self.logger.info("Search item found. Test passed.")
            assert True
        except:
            self.driver.save_screenshot("/Users/vivekkumar/screenshots/test_search_failed.png")
            self.logger.error("Search failed or element not found. Screenshot captured.")
            assert False

        self.logger.info("====== Test_004_Search Completed ======")