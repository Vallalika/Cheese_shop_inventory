import unittest
from models.provider import Provider

class TestProvider(unittest.TestCase):
    
    def setUp(self):
        self.normandie = Provider("Normandie", "Farmer", "France", "A Normandy village")
    
    def test_provider_has_name(self):
        self.assertEqual("Normandie", self.normandie.name)
        
        
    def test_provider_has_type(self):
        self.assertEqual("Farmer", self.normandie.type)
        
    def test_provider_has_country(self):
        self.assertEqual("France", self.normandie.country)
    
    def test_provider_has_address(self):
        self.assertEqual("A Normandy village", self.normandie.address)
        
    def test_provider_has_no_cheese(self):
        self.assertIsNone(self.normandie.cheeses)
    
    def test_provider_has_no_id_yet(self):
        self.assertIsNone(self.normandie.id)