from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class WaitForElement:
    @staticmethod
    def wait(driver, id, time_out=100):
        try:
            WebDriverWait(driver, time_out).until(
                lambda driver: driver.find_element(*id))
        except TimeoutException:
            print('Not able to find ID:' + id)
