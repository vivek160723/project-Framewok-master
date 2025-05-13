import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Recruit:
    def __init__(self,driver):
        self.driver=driver
        time.sleep(5)
        self.username_box = (By.NAME, "username")
        self.password_box = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.recruitementbutton=(By.XPATH, "//span[text()='Recruitment']")
        self.addbutton = (By.XPATH, "//button[normalize-space()='Add']")
        self.firstname = (By.NAME, "firstName")
        self.lastname = (By.NAME, "lastName")
        self.email = (By.XPATH, "//label[text()='Email']/../following-sibling::div/input")
        self.jobvacancydd= (By.XPATH, "//label[text()='Vacancy']/../following-sibling::div//div[contains(@class, 'oxd-select-text')]")
        self.vacancy= (By.XPATH, "//div[@role='option']/span[text()='Software Engineer']")  # Example
        self.savebutton= (By.XPATH, "//button[normalize-space()='Save']")
        self.successmessage= (By.XPATH, "//div[contains(@class,'oxd-toast-content')]")

    def enterUserName(self, username):
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

    def clickrecruitment(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button)
        ).click()

    def clickaddbutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button)
        ).click()

    def clickfirstname(self,fname):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.firstname)
        ).send_keys(fname)

    def clicklastname(self,lname):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.lastname)
        ).send_keys(lname)

    def clickemailid(self,eid):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email)
        ).send_keys(eid)

    def clickjobvacancydd(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.jobvacancydd)
        ).click()

    def clickvacancy(self,vcy):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.vacancy)
        ).send_keys(vcy)

    def clicksavebutton(self):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.savebutton)
    ).click()

    def getsuccessmessage(self):
        e=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.successmessage)
        )
        return e.text


