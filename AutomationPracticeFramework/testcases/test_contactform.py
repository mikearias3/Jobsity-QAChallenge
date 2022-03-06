import unittest
from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen
from pageobjects.contactusform import ContactUsForm


class ContactUsFormTestSuite(unittest.TestCase):

	def setUp(self):
		self.driver = Driver()
		self.driver.navigate(strings.base_url)

	def test_contact_us_form_components_are_visible(self):
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

	def test_contact_us_subject_field_validation_for_empty_subject(self):
		self.homescreen = HomeScreen(self.driver)
		self.homescreen.click_contact_us_button()

		self.contact_us_form = ContactUsForm(self.driver)
		self.contact_us_form.write_email_address(strings.valid_email)
		self.contact_us_form.write_message(strings.valid_message)
		self.contact_us_form.click_send_button()
		self.contact_us_form.validate_error_message(strings.missing_subject_error)

	def test_contact_us_email_validation_for_empty_email(self):
		self.homescreen = HomeScreen(self.driver)
		self.homescreen.click_contact_us_button()

		self.contact_us_form = ContactUsForm(self.driver)
		self.contact_us_form.select_subject_heading(strings.subject)
		self.contact_us_form.write_message(strings.valid_message)
		self.contact_us_form.click_send_button()
		self.contact_us_form.validate_error_message(strings.invalid_email_error)

	def test_contact_us_email_validation_for_invalid_email(self):
		self.homescreen = HomeScreen(self.driver)
		self.homescreen.click_contact_us_button()

		self.contact_us_form = ContactUsForm(self.driver)
		self.contact_us_form.select_subject_heading(strings.subject)
		self.contact_us_form.write_email_address(strings.invalid_email)
		self.contact_us_form.write_message(strings.valid_message)
		self.contact_us_form.click_send_button()
		self.contact_us_form.validate_error_message(strings.invalid_email_error)

	def test_contact_us_message_validation_for_empty_message(self):
		self.homescreen = HomeScreen(self.driver)
		self.homescreen.click_contact_us_button()

		self.contact_us_form = ContactUsForm(self.driver)
		self.contact_us_form.select_subject_heading(strings.subject)
		self.contact_us_form.write_email_address(strings.valid_email)
		self.contact_us_form.click_send_button()
		self.contact_us_form.validate_error_message(strings.missing_message_error)

	def tearDown(self):
		self.driver.instance.quit()


if __name__ == '__main__':
	unittest.main()
