import unittest

import unh698

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = unh698.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'UNH698 Website' in rv.data
    def test_link_to_my_page(self):
        rv = self.app.get('/')  
        # Search the page contents for the link to your topic page 
        # Replace xxxxxxxxxxxx with text you'd expect to see on your main page that links to your subpage
        assert b'boring 1' in rv.data
    def test_link_to_my_page_2(self):
        rv = self.app.get('/')  
        # Search the page contents for the link to your topic page 
        # Replace xxxxxxxxxxxx with text you'd expect to see on your main page that links to your subpage
        assert b'boring 2' in rv.data
"""
    def test_my_topic(self):
        # Replace '/' with the page path you want to make
        rv = self.app.get('/topic1')  
        # Replace UNH698 Website with the text you expect to see on you topic page
        assert b'I am bored' in rv.data
    def test_my_topic_2(self):
        # Replace '/' with the page path you want to make
        rv = self.app.get('/topic2')  
        # Replace UNH698 Website with the text you expect to see on you topic page
        assert b'I am bored 2' in rv.data
"""
if __name__ == '__main__':
unittest.main()