import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID,"id_list_table")
        rows = table.find_elements(By.TAG_NAME ,"tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_title(self):
        self.browser.get(self.live_server_url)
        title = self.browser.title
        self.assertIn("To-Do", self.browser.title)

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn("To-Do", self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # first item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # second item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
        time.sleep(3)

        self.fail("Finish the test!")

        # TODO
        #   clean up after FT runs

if __name__ == "__main__":
    if __name__ == '__main__':
        LiveServerTestCase.run()
