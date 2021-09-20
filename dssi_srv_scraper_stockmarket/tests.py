"""DSSi comment: standard package """
from django.test import TestCase
import requests

# Create your tests here.
class srv_scraper_stockmarket(TestCase):

    def test_check_request_status_ok(self):
        self.vr_requests = requests.get('https://www.investing.com/equities/microsoft-corp')
        print(f"test_check_request_status_ok {self.assertEqual(self.vr_requests.status_code, 200)}")

    def test_check_request_status_ko(self):
        self.vr_requests = requests.get('https://www.investing.com/equities/microsoft-corp123')
        print(f"test_check_request_status_ko {self.assertEqual(self.vr_requests.status_code, 404)}")
        
