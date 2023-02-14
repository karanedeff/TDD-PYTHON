from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_title(self):
        self.browser.get("http://127.0.0.1:8000")
        title = self.browser.title
        self.assertIn("success",self.browser.title)

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000")

        self.assertIn("To-Do", self.browser.title)
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

