import unittest
import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_title(self):
        self.browser.get("http://127.0.0.1:8000")
        title = self.browser.title
        self.assertIn("To-Do",self.browser.title)

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000")

        self.assertIn("To-Do", self.browser.title)

        header_text =  self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do",header_text)

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        time.sleep(3)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # self.assertTrue(
        #     any(row.text == "1: Buy peacock feathers" for row in rows),
        #     f"New to-do item did not apper in table. Contents were:\n{table.text}"
        # )
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn("2: Use peacock feathers to make a fly", [row.text for row in rows])

        self.fail("Finish the test!")

if __name__ == "__main__":
    unittest.main(warnings="ignore")
    # invite to add

    # type into box

    # page update on enter, new item

    # add another

    # update again

    # unique url, save state, help

    # return to url

    # end

