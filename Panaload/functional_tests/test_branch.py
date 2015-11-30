from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from .test import FunctionalTest

class FunctionalTest2(FunctionalTest):

	fixtures = ['admin_user.json']
	def test_can_create_branch_via_Admin(self):

		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		Uusername_field = self.browser.find_element_by_name('username')
		Uusername_field.send_keys('gerald')

		Upassword_field = self.browser.find_element_by_name('password')
		Upassword_field.send_keys('1')
		Upassword_field.send_keys(Keys.RETURN)

		hyper_branch = self.browser.find_elements_by_link_text('Branches')
		self.assertEquals(len(hyper_branch),1)



		hyper_branch[0].click()
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Branches', body.text)

		add_branch = self.browser.find_element_by_link_text('Add branch')
		add_branch.click()

		BranchName = self.browser.find_element_by_name('BranchName')
		BranchName.send_keys("Cebuana Lhuilhier Las Pinas Talon II")

		BranchAddress = self.browser.find_element_by_name('BranchAddress')
		BranchAddress.send_keys("Talon II, Las Pinas City")

		BranchContactNo = self.browser.find_element_by_name('BranchContactNo')
		BranchContactNo.send_keys("09478155576")

		save = self.browser.find_element_by_css_selector("input[value='Save']")
		save.click()