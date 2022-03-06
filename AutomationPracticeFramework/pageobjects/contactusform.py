from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUsForm:

	def __init__(self, driver):
		self.driver = driver
		self.title = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.XPATH, "//h1[contains(text(), 'Customer service - Contact us')]")))
		self.heading = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.XPATH, "//h3[contains(text(), 'send a message')]")))
		self.subject_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "uniform-id_contact")))
		self.subject_dropdown = Select(self.driver.instance.find_element_by_id('id_contact'))
		self.email_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "email")))
		self.order_reference_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "id_order")))
		self.attach_file_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "uniform-fileUpload")))
		self.message_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "message")))
		self.send_button = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "submitMessage")))

	def validate_form_title_is_present(self):
		assert self.title, "Contact Us Form Title is not visible"

	def validate_form_heading_is_present(self):
		assert self.heading, "Contact Us Heading is not visible"

	def validate_subjectf_field_is_present(self):
		assert self.subject_field, "Subject Field is not visible"

	def validate_email_field_is_present(self):
		assert self.email_field, "Email Field is not visible"

	def validate_order_reference_field_is_present(self):
		assert self.order_reference_field, "Order Reference Field is not visible"

	def validate_attach_file_field_is_present(self):
		assert self.attach_file_field, "Attach File Field is not visible"

	def validate_message_field_is_present(self):
		assert self.message_field, "Message Field is not visible"

	def write_email_address(self, email):
		self.email_field.send_keys(email)

	def write_message(self, message):
		self.message_field.send_keys(message)

	def click_send_button(self):
		self.send_button.click()

	def validate_error_message(self, error):
		error_message = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.XPATH, "//li[contains(text(), '{0}')]".format(error))))

	def select_subject_heading(self, subject):
		self.subject_dropdown.select_by_visible_text(subject)

	def write_order_reference(self, order_reference):
		self.order_reference_field.send_keys(order_reference)
