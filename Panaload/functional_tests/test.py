from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

class FunctionalTest(LiveServerTestCase):
	fixtures = ['admin_user.json']

	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()




	def get_username(self):
		return self.browser.find_element_by_id('id_username')

	def get_password(self):
		return self.browser.find_element_by_id('id_password')


if __name__ == '__main__':
    _test()


