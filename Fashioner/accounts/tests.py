from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(executable_path=r'E:\chromedriver_win32\chromedriver.exe')
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        time.sleep(300)
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/accounts/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit=selenium.find_element_by_name('submit')

        #Fill the form with data
        username.send_keys('fashion')
        password.send_keys('fashion')
        
        time.sleep(3000)
        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        
        # assert 'Check your email' in selenium.page_source
