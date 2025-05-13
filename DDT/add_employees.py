import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageobjects.LoginPage import Login
from pageobjects.PimPage import Pim

# Load Excel data
df = pd.read_excel(r"C:\Users\divya aghi\Downloads\employee_data (1).xlsx")

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
login_page = Login(driver)
login_page.enterUserName("Admin")
login_page.setPassword("admin123")
login_page.clickLogin()
WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
print("✅ Logged in successfully!")

# Initialize PIM page object
pim_page = Pim(driver)

# Iterate through employee data
for index, row in df.iterrows():
        first_name = row['First Name']
        middle_name=row['Middle Name']
        last_name = row['Last Name']
        employee_id = str(row['Employee ID'])
        pim_page.clickpimbutton()
        pim_page.clickaddbutton()
        pim_page.addfirstname(first_name)
        pim_page.addmiddlename(middle_name)
        pim_page.addlastname(last_name)
        pim_page.addemployeeid(employee_id)
        pim_page.clicksavebutton()
        print(f"✅ Employee added successfully.")

driver.quit()
