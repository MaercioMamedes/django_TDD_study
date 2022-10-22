from django.test import LiveServerTestCase
from selenium import webdriver
import os


class AnimalsTestCase(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(os.path.abspath('chromedriver'))

    def tearDown(self) -> None:
        self.browser.quit()

    def test_open_window_of_the_chrome(self):
        self.browser.get(self.live_server_url)


