from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrive_it_later(self):
        
        #Edith heard about a new interesting app that sets "To do" lists
        #She checks its homepage
        self.browser.get("http://localhost:8000")

        #In the title she reads "To do"
        self.assertIn("To-do", self.browser.title)

        #She is likely to insert an item in the list
        #She writes "Buy peacock feathers" in a text box

        #When she hits "Enter" the page refreshes and lists
        #"1: Buy peacock feathers"

        #The page still show an text box invites Edith to insert another item
        #Edith types "Use peacock feathers to make a fly"

        #The page refreshs again and shows two itens

        #Edith wonders if the site remembers her list. So the site generated a url

        #She access the url and her list remains there

        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

