import time

from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By

from utils.browser import get_chrome_driver


class SocialEchoBaseFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.browser = get_chrome_driver()
        self.browser.get(self.live_server_url)

        return super().setUp()

    def tearDown(self):
        self.browser.quit()

        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)


class SocialEchoHomePageFunctionalTest(SocialEchoBaseFunctionalTest):
    def test_social_echo_home_page_h1_is_correct(self):
        body = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Social Echo', body.text)
        self.sleep()
