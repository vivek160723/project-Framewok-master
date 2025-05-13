import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pim:
    def __init__(self,driver):
        self.driver=driver
        time.sleep(5)
        self.username_box = (By.NAME, "username")

        self.password_box = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.pim_button=(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
        self.add_button=(By.XPATH,"//button[text()=' Add ']")
        self.first_name=(By.NAME,"firstName")
        self.middle_name=(By.NAME,"middleName")
        self.last_name=(By.NAME,"lastName")
        self.employee_id=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
        self.save_button=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")

    def enterUserName(self,username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_box)
        ).send_keys(username)

    def setPassword(self, password):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_box)
            ).send_keys(password)

    def clickLogin(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_button)
            ).click()

    def clickpimbutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.pim_button)
        ).click()


    def clickaddbutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.add_button)
        ).click()


    def addfirstname(self,fn):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name)
        ).send_keys(fn)


    def addmiddlename(self,mn):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.middle_name)
        ).send_keys(mn)

    def addlastname(self,ln):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.last_name)
        ).send_keys(ln)

    def addemployeeid(self,id):
        ef=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.employee_id)
        )
        ef.clear()
        ef.send_keys(id)


    def clicksavebutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.save_button)
        ).click()

