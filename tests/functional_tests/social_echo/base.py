import time

from django.test import LiveServerTestCase

from utils.base_for_tests.base_for_post import BaseCreatePost
from utils.browser import get_chrome_driver


class SocialEchoBaseFunctionalTest(LiveServerTestCase, BaseCreatePost):
    def setUp(self):
        self.browser = get_chrome_driver(False)
        self.browser.get(self.live_server_url)

        return super().setUp()

    def tearDown(self):
        self.browser.quit()

        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)
