from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

print("hi")

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()



    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID,'id_list_table')
                rows = table.find_elements(By.TAG_NAME,'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    
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
        

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        
        
        
        #The page still show an text box invites Edith to insert another item
        #Edith types "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly') 
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        

        
        
        #The page refreshs again and shows two itens

        #Edith wonders if the site remembers her list. So the site generated a url

        #She access the url and her list remains there

    def test_multiple_user_can_start_at_different_urls(self):
        # Edith starts a new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #She notes that her list has a unique URL
        edith_list_ult = self.browser.current_url
        self.assertRegex(edith_list_ult, '/lists/.+')

        #Now a new user access the website
        self.browser.quit()
        self.browser = webdriver.Firefox()
    
        #Francis access the home page and there is no clue of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #Francis starts a new list
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        #Francis get its own url
        francis_list_ult = self.browser.current_url
        self.assertRegex(francis_list_ult, '/lists/.+')
        # self.assertEqual(francis_list_ult, edith_list_ult)

        #There is no clue of Edith's list after all
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        self.fail('Finish the test!')
        



