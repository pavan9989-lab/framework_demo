import pytest
from selenium import webdriver


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.log_in = Login()
        print("class lable setup logging in ")
        yield
        print('logging out')


    def test_tc123_verify_login_screen(self):
        assert self.log_in.login_to_account()
        assert self.log_in.verify_login()