from selenium import webdriver

class Login():

    __username = "username"
    __password = "password"
    __login_button = "//input[@type='submit']"
    __your_project = "//*[contains(test(),'Your projects (O)')]"


    def __init__(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/drivers/chromedriver.exe")


    def login_to_account(self):
        driver.get("https://pypi.org/account/login/")
        driver.find_element_by_id(self.__username).send_keys("govind3011")
        driver.find_element_by_id(self.__password).send_keys("govind@3011")
        driver.find_element_by_id(self.__login_button).click()
        print("login successful")

    def verify_login(self):
        return driver.find_element_by_xpath(self.__your_project).is_displayed()




