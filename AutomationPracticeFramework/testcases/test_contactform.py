import unittest
from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen
from pageobjects.contactusform import ContactUsForm


class ContactUsFormTestSuite(unittest.TestCase):

	def setUp(self):
		self.driver = Driver()
		self.driver.navigate(strings.base_url)

	def test_contact_us_form_components(self):
		self.homescreen = HomeScreen(self.driver)
		self.homescreen.click_contact_us_button()

		self.contact_us_form = ContactUsForm(self.driver)
		self.contact_us_form.validate_form_title_is_present()
		self.contact_us_form.validate_form_heading_is_present()
		self.contact_us_form.validate_subjectf_field_is_present()
		self.contact_us_form.validate_email_field_is_present()
		self.contact_us_form.validate_order_reference_field_is_present()
		self.contact_us_form.validate_attach_file_field_is_present()
		self.contact_us_form.validate_message_field_is_present()

	def tearDown(self):
		self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
