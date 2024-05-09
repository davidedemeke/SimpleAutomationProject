from selenium.webdriver.support import expected_conditions as ec
from automation_ui_module.base_element import BaseElement
from automation_ui_module.locators.calendar_locators import CalenderLocators


class CalenderPage(BaseElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://stephenchou1017.github.io/scheduler/#/'

    def click_infinite_button(self):
        self.wait.until(ec.element_to_be_clickable(CalenderLocators.INFINITE_SCROLL)).click()

    def click_month_button(self):
        self.wait.until(ec.element_to_be_clickable(CalenderLocators.MONTH_BTN)).click()

    def get_event_elements_count(self):
        return self.wait.until(ec.visibility_of_all_elements_located(CalenderLocators.ALL_EVENTS))

    def create_event(self):
        event = self.wait.until(ec.element_to_be_clickable(CalenderLocators.CREATE_EVENT)).click()
        alert = event.switch_to.alert
        # Accept the alert (click OK button)
        alert.accept()
