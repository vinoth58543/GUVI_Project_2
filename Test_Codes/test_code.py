from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from  Test_Data import data
from Test_Locator import locator
from selenium.common.exceptions import NoSuchElementException

class Test_vinoth:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    #script for forgot password
    def test_login(self,booting_function):
        try:
           self.driver.get(data.Data().url)
           #implict wait used
           self.driver.implicitly_wait(10)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().forgot_your_password).click()
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().reset_button).click()
        except:
            print('error occured')

    #script for titles
    def test_title(self,booting_function):
        try:
           self.driver.get(data.Data().url)
           #implict wait used
           self.driver.implicitly_wait(10)
           self.driver.maximize_window()
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.NAME, value=locator.Locators().password_input_box).send_keys(data.Data().password)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().submit_button).click()
           self.driver.find_element(by=By.XPATH, value=locator.Locators().admin).click()
        except:
            print('error occured')
    
        
    
        expected_list = ['User Management','Jobs','Organization','Qualifications','Nationalites','Corporate Branding','Configuration']
        web_element =self.driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li')
        for i in web_element:
            if i.text in expected_list:
                print(i.text, "Is present")
    


    #script for main menu title
    def test_main(self,booting_function):
        try:
           self.driver.get(data.Data().url)
           self.driver.implicitly_wait(10)
           self.driver.maximize_window()
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.NAME, value=locator.Locators().password_input_box).send_keys(data.Data().password)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().submit_button).click()
        except:
            print('error occured')
        
    
        expected_list = ['Admin','PIM','Leave','Time','Recruitment','My Info','Performance','Dashboard','Directory','Maintenance','Buzz']
        web_element =self.driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li')
        for i in web_element:
            if i.text in expected_list:
                print(i.text, "Is present")







        
        


        