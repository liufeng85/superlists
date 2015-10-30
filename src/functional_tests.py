# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪丝听说有一个很酷的在线待办事项应用
        #她去首页看了这个应用
        self.browser.get('http://localhost:8000')
        self.assertIn('to-do',self.browser.title)
        self.fail('Finish the test!')
'''      
if __name__ =='__main__':
    unittest.main()
'''