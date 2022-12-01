from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

print("hi")

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertIn(row_text, [row.text for row in rows])

    
    def test_can_start_a_list_and_retrive_it_later(self):
        
        #Edith heard about a new interesting app that sets "To do" lists
        #She checks its homepage
        self.browser.get(self.live_server_url)

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

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        
        
        
        #The page still show an text box invites Edith to insert another item
        #Edith types "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly') 
        

        
        
        #The page refreshs again and shows two itens

        #Edith wonders if the site remembers her list. So the site generated a url

        #She access the url and her list remains there
        self.fail('Finish the test!')
        



