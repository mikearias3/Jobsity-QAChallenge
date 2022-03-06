from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUsForm:

	def __init__(self, driver):
		self.driver = driver
		self.title = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located(
				By.XPATH("//h1[contains(text(), 'Customer service - Contact us')]")))
		self.heading = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located(
				By.XPATH("//h3[contains(text(), 'send a message')]")))
		self.subject_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located(
				By.ID("id_contact")))
		self.email_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located(
				By.ID("email")))
		self.order_reference_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located(
				By.ID("id_order")))
		self.attach_file_field = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located(
				By.ID("fileUpload")))
		self.message_field = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(By.ID("message")))

	def validate_form_title_is_present():
		assert self.title, "Contact Us Form Title is not present"

	def validate_form_heading_is_present():
		assert self.heading, "Contact Us Heading is not present"

	def validate_subjectf_field_is_present():
		assert self.subject_field, "Subject Field is not present"

	def validate_email_field_is_present():
		assert self.email_field, "Email Field is not present"

	def validate_order_reference_field_is_present():
		assert self.order_reference_field, "Order Reference Field is not present"

	def validate_attach_file_field_is_present():
		assert self.attach_file_field, "Attach File Field is not present"

	def validate_message_field_is_present():
		assert self.message_field, "Message Field is not present"
