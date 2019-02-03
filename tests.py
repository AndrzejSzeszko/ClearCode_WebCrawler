#!/usr/bin/python3.7
import unittest
from WebScraper import site_map


class WebScraperTestCase(unittest.TestCase):
    """
    1) NAVIGATE TO example/ DIRECTORY!!!
    2) RUN "python -m http.server" COMMAND BEFORE RUNNING TESTS!!!
    """
    def setUp(self):
        self.test_url = 'http://0.0.0.0:8000/'
        self.correct_result = {
            'http://0.0.0.0:8000': {
                'title': 'Index',
                'links': {'http://0.0.0.0:8000/example.html', 'http://0.0.0.0:8000/site.html'}
            },
            'http://0.0.0.0:8000/site.html': {
                'title': 'The Site',
                'links': {'http://0.0.0.0:8000/site/subsite.html'}
            },
            'http://0.0.0.0:8000/example.html': {
                'title': 'No links here',
                'links': set()
            },
            'http://0.0.0.0:8000/site/subsite.html': {
                'title': 'Looping',
                'links': {'http://0.0.0.0:8000/site/other_site.html', 'http://0.0.0.0:8000'}
            },
            'http://0.0.0.0:8000/site/other_site.html': {
                'title': 'Looped',
                'links': {'http://0.0.0.0:8000/site/subsite.html'}
            }
        }

    def tearDown(self):
        pass

    def test_site_map(self):
        self.assertEqual(self.correct_result, site_map(self.test_url))


if __name__ == '__main__':
    unittest.main()
