import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.Recruitment import Recruit
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class Test_005_Recruitement:
    def setup_method(self):
        config = ReadConfig()
        self.base_url = config.getApplicationURL()
        self.username = config.getUsername()
        self.password = config.getPassword()
        self.fname = "Anjali"
        self.lname = "Aghi"
        self.eid = "anjaliaghi56@example.com"
        self.vcy = "Payroll Administrator"

    def test_recruitement(self):
        self.driver.get(self.base_url)
        self.r = Recruit(self.driver)

        # Login
        self.r.enterUserName(self.username)
        self.r.setPassword(self.password)
        self.r.clickLogin()

        # Wait for dashboard to load
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )

        # Navigate to Recruitment and Add Candidate
        self.r.clickrecruitment()
        self.r.clickaddbutton()
        self.r.clickfirstname(self.fname)
        self.r.clicklastname(self.lname)
        self.r.clickemailid(self.eid)
        self.r.clickjobvacancydd()
        self.r.clickvacancy(self.vcy)
        self.r.clicksavebutton()

        # Wait for confirmation or redirection
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Successfully Saved')]"))
        )

        print("✅ Candidate successfully added")