from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report
import unittest
def test_citaions_needed_count():
    actual=get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    expected=5
    assert actual==expected

def test_citations_needed_count_zero():
    actual=get_citations_needed_count('https://en.wikipedia.org/wiki/Lake_Texcoco')
    expected=0
    assert actual==expected

def test_citaions_needed_report():
    actual=get_citations_needed_report('https://en.wikipedia.org/wiki/Harpsichord')
    expected='Two of the most prominent composers of the Classical era, Joseph Haydn (1732–1809) and Wolfgang Amadeus Mozart (1756–1791), wrote harpsichord music. For both, the instrument featured in the earlier period of their careers, and although they had come into contact with the piano later on, they nonetheless continued to play the harpsichord and clavichord for the rest of their lives. Mozart was noted to have played his second last keyboard concerto (the "Coronation") on the harpsichord.[citation needed] \n'

def test_citaions_needed_report_zero():
    actual=get_citations_needed_report('https://en.wikipedia.org/wiki/Lake_Texcoco')
    expected="No citation needed"
    assert actual == expected
class Testscraper(unittest.TestCase):
    def test_not_wiki_page(self):
        with self.assertRaises(Exception):
            get_citations_needed_count('https://www.google.jo/?hl=ar')
            get_citations_needed_report('https://www.google.jo/?hl=ar')
    