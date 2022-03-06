import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeScreen:

	def __init__(self, driver):
		self.driver = driver
		self.contact_us_button = WebDriverWait(self.driver.instance, 10).until(
			EC.visibility_of_element_located((
				By.ID, "contact-link")))

	@allure.step("Click Contact Us Button")
	def click_contact_us_button(self):
		self.contact_us_button.click()
