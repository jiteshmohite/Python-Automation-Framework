import unittest

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import desired_capabilities

"""
TODO: In-Progress, Refer page object model
"""


class FindByImageTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_based_on_image_template(self):
        image_path = desired_capabilities.PATH('find_by_image_success.png')
        el = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.IMAGE, image_path))
        )
        size = el.size
        self.assertIsNotNone(size['width'])
        self.assertIsNotNone(size['height'])
        loc = el.location
        self.assertIsNotNone(loc['x'])
        self.assertIsNotNone(loc['y'])
        rect = el.rect
        self.assertIsNotNone(rect['width'])
        self.assertIsNotNone(rect['height'])
        self.assertIsNotNone(rect['x'])
        self.assertIsNotNone(rect['y'])
        self.assertTrue(el.is_displayed())
        el.click()
        self.driver.find_element_by_accessibility_id("Alarm")

    def test_find_multiple_elements_by_image_just_returns_one(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "App"))
        )
        image_path = desired_capabilities.PATH('find_by_image_success.png')
        els = self.driver.find_elements_by_image(image_path)
        els[0].click()
        self.driver.find_element_by_accessibility_id("Alarm")

    def test_find_throws_no_such_element(self):
        image_path = desired_capabilities.PATH('find_by_image_failure.png')
        with self.assertRaises(TimeoutException):
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.IMAGE, image_path))
            )
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_image(image_path)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByImageTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
