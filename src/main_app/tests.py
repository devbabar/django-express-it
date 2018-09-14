from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class ExpressItTestCase(LiveServerTestCase):

	def setUp(self):
		User.objects.create_user(username="babar",password="babar1234")
		self.selenium = webdriver.Firefox()
		self.selenium.maximize_window()
		super(ExpressItTestCase, self).setUp()

	def tearDown(self):
		# self.selenium.quit()
		super(ExpressItTestCase, self).tearDown()


	'''Expected Result: Should click on registerlink and register New User '''
	def test_register(self):
		selenium = self.selenium
		#Opening the link we want to test
		selenium.get('http://127.0.0.1:8000/signup')
		# selenium.get('%s%s' % (self.live_server_url,'/signup/'))
		#find the form element
		username = selenium.find_element_by_id('id_username')
		first_name = selenium.find_element_by_id('id_first_name')
		last_name = selenium.find_element_by_id('id_last_name')
		email = selenium.find_element_by_id('id_email')
		password1 = selenium.find_element_by_id('id_password1')
		password2 = selenium.find_element_by_id('id_password2')
		# submit = selenium.find_element_by_name('register')

		#Fill the form with data
		username.send_keys('andy2')
		first_name.send_keys('andy')
		last_name.send_keys('smith')  
		email.send_keys('andy@live.com')
		password1.send_keys('andy123456')
		password2.send_keys('andy123456')

		#submitting the form
		# submit.send_keys(Keys.RETURN)
		# submit.click()
		selenium.find_element_by_xpath('//button[@name="register"]').click()
		# submit.send_keys(Keys.ENTER)

		# selenium.get('%s%s' % (self.live_server_url,'/logout/'))
		selenium.find_element_by_id('home_username').click()
		selenium.find_element_by_name('logout').click()
		#check the returned result
		# assert 'login' in selenium.page_source
		# assert 'register' in selenium.page_source
		# assert 'wrong confirmation' in selenium.page_source


	'''Expected Result: It should go to login page, fill credentials and click on login button '''
	def test_login(self):
		selenium = self.selenium
		#Opening the link we want to test
		# selenium.get('%s%s' % (self.live_server_url,'/accounts/login/'))
		selenium.get('http://127.0.0.1:8000/accounts/login/')
		selenium.get('%s%s' % (self.live_server_url,'/accounts/login/'))
		username_input = selenium.find_element_by_id("id_username")
		password_input = selenium.find_element_by_id("id_password")
		login_click = selenium.find_element_by_name("login")

		username_input.send_keys("babar")
		password_input.send_keys("babar1234")
		login_click.click()


	'''Expected Result: It should go to login page, click at Register link underneath of login fields and register New User '''
	def test_login_page_registration_link(self):
		selenium = self.selenium
		#Opening the link we want to test
		# selenium.get('%s%s' % (self.live_server_url,'/accounts/login/'))
		selenium.get('http://127.0.0.1:8000/accounts/login/')
		link = selenium.find_element_by_name("login_page_registration_link")
		link.click()

		#find the form element
		username = selenium.find_element_by_id('id_username')
		first_name = selenium.find_element_by_id('id_first_name')
		last_name = selenium.find_element_by_id('id_last_name')
		email = selenium.find_element_by_id('id_email')
		password1 = selenium.find_element_by_id('id_password1')
		password2 = selenium.find_element_by_id('id_password2')

		#Fill the form with data
		username.send_keys('andy1')
		first_name.send_keys('andy')
		last_name.send_keys('smith')  
		email.send_keys('andy@live.com')
		password1.send_keys('andy123456')
		password2.send_keys('andy123456')

		#submitting the form
		selenium.find_element_by_xpath('//button[@name="register"]').click()


	'''Expected Result: It should not allow to view User profile and redirect to login page '''
	def test_user_profile_without_login(self):
		selenium = self.selenium
		#Opening the link we want to test
		selenium.get('%s%s' % (self.live_server_url,'/'))
		selenium.get('http://127.0.0.1:8000')
		# selenium.get('%s%s' % (self.live_server_url,'/accounts/login/'))
		username_link = selenium.find_element_by_id("username-link")
		username_link.click()







