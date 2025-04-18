from selenium.webdriver.common.by import By

from .base import SocialEchoBaseFunctionalTest


class SocialEchoHomePageFunctionalTest(SocialEchoBaseFunctionalTest):
    def test_social_echo_home_page_h1_is_correct(self):
        body = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Social Echo', body.text)
        self.sleep()
