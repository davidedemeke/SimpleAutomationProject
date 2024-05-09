import random

import allure
import pytest
from selenium import webdriver
from automation_ui_module.pages.calender_page import CalenderPage

@allure.story("Story Name")
@allure.title("Test UI for opening and creating event in calender")
class TestCalendarCreation:
    @pytest.fixture(scope="module")
    def driver(self):
        # Initialize the browser
        driver = webdriver.Chrome()
        yield driver
        # Close the browser
        driver.quit()

    def test_create_events_and_validate_data(self, driver):
        """
        Test to create events on the calendar page and verify DOM element count.

        Steps:
        1. Initialize the calendar page.
        2. Navigate to the calendar webpage.
        3. Click on the "Infinite" button.
        4. Click on the "Month" button.
        5. Create a random number of new events (between 1 and 5) and check DOM element count.
        6. Verify that the DOM element count increased after creating events.
        7. Navigate back to the original data.
        8. Check if the events still exist in the DOM.

        Args:
        - self: Test class instance.
        - driver: WebDriver instance for browser automation.
        """
        calendar_page = CalenderPage(driver)

        driver.get("https://stephenchou1017.github.io/scheduler/#/")
        calendar_page.click_infinite_button()
        calendar_page.click_month_button()

        initial_count = calendar_page.get_event_elements_count()
        for _ in range(random.randint(1, 5)):  # Randomly create event between 1 and 5 events
            calendar_page.create_event()

        new_count = calendar_page.get_event_elements_count()
        assert new_count > initial_count, "DOM element count did not increase after creating events"

        driver.back()
        events_exist = calendar_page.get_event_elements_count() > 0
        assert events_exist, "Events created in step 5 no longer exist after navigating back to original data"
