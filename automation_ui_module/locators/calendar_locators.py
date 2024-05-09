from selenium.webdriver.common.by import By


class CalenderLocators(object):
    """
    //a[contains(@href, '#/infinitescroll')]/span[text()='Infinite scroll']
    """

    INFINITE_SCROLL = (By.XPATH, "//a[contains(@href, '#/infinitescroll')]/span[text()='Infinite scroll']")
    MONTH_BTN = (By.XPATH, "//span[contains(text(), 'Month')]")
    ALL_EVENTS = (By.CSS_SELECTOR, "table.scheduler-content-table")
    CREATE_EVENT = (By.CSS_SELECTOR, "div.event-container:first-child")
