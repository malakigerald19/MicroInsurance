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

	def test_can_create_branch_via_Admin(self):

		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		Uusername_field = self.browser.find_element_by_name('username')
		Uusername_field.send_keys('gerald')

		Upassword_field = self.browser.find_element_by_name('password')
		Upassword_field.send_keys('1')
		Upassword_field.send_keys(Keys.RETURN)

		hyper_branch = self.browser.find_elements_by_link_text('Branchs')
		self.assertEquals(len(hyper_branch),1)



		hyper_branch[0].click()
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('branchs', body.text)

		add_branch = self.browser.find_element_by_link_text('Add branch')
		add_branch.click()

	def get_username(self):
		return self.browser.find_element_by_id('id_username')

	def get_password(self):
		return self.browser.find_element_by_id('id_password')


if __name__ == '__main__':
    _test()


