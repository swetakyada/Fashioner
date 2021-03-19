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
        selenium.get('http://127.0.0.1:8000/accounts/signup/')
        #find the form element
        first_name = selenium.find_element_by_name('first_name')
        last_name = selenium.find_element_by_name('last_name')
        username = selenium.find_element_by_name('username')
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')
        submit = selenium.find_element_by_name('signup')

        #Fill the form with data
        username.send_keys('unary')
        first_name.send_keys('Yusuf')
        last_name.send_keys('Unary')
        email.send_keys('contact@yusuf.im')
        password1.send_keys('123456')
        password2.send_keys('123456')
        time.sleep(3000)
        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert email.text == 'contact@yusuf.im'
        # assert 'Check your email' in selenium.page_source