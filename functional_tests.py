from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

print("hi")

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
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-do', header_text)

        #She is likely to insert an item in the list
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        #She writes "Buy peacock feathers" in a text box
        inputbox.send_keys('Buy peacock feathers')

        #When she hits "Enter" the page refreshes and lists
        #"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table")
        #The page still show an text box invites Edith to insert another item
        #Edith types "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
        #The page refreshs again and shows two itens

        #Edith wonders if the site remembers her list. So the site generated a url

        #She access the url and her list remains there

        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

