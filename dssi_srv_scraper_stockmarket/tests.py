"""DSSi comment: standard package """
from django.test import TestCase
import requests
from bs4 import BeautifulSoup

# Create your tests here.
class srv_scraper_stockmarket(TestCase):

    def test_check_request_status_ok(self):
        self.vr_requests = requests.get('https://www.investing.com/equities/microsoft-corp')
        print(f"test_check_request_status_ok {self.assertEqual(self.vr_requests.status_code, 200)}")

    def test_check_request_status_ko(self):
        self.vr_requests = requests.get('https://www.investing.com/equities/microsoft-corp123')
        print(f"test_check_request_status_ko {self.assertEqual(self.vr_requests.status_code, 404)}")
    
    def test_check_content_have_stockname(self):
        vr_soupb = (BeautifulSoup(requests.get('https://www.investing.com/equities/microsoft-corp').text, 'html.parser')).find_all("h1")
        vr_name_exits = False
        for span_tag_attr in vr_soupb:
            if 'instrument-header_title__GTWDv' in str(span_tag_attr.get("class")):
                vr_name_exits = True
                break
        print(f"test_check_content_have_stockname {self.assertTrue(vr_name_exits)}")  
            
    def test_check_content_have_stockvalue(self):
        vr_soupb = (BeautifulSoup(requests.get('https://www.investing.com/equities/microsoft-corp').text, 'html.parser')).find_all("span")
        vr_value_exits = False
        for span_tag_attr in vr_soupb:
            if 'instrument-price_last__KQzyA' in str(span_tag_attr.get("class")):
                vr_value_exits = True
                break
        print(f"test_check_content_have_stockvalue {self.assertTrue(vr_value_exits)}")            
