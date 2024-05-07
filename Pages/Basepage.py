from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage():
    
    def __init__(self,driver):
        self.driver = driver

    def enter_text(self,locator,text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        