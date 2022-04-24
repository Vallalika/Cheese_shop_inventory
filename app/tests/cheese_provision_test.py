import unittest
from models.cheese_provision import cheese_provision
from models.cheese import Cheese
from models.provider import Provider

class TestCheeseProvision(unittest.TestCase):
    
    def setUp(self):
        self.camembert = Cheese("Camembert", "France", "Raw Cow's Milk", "Fine velvety rind marked by brown-red streaks. Light yellow interior. Supple texture. Aromas of forest floor, mushroom and earth after ripening. Milky and tart notes.", 20, 5.00, 8.00)
        self.normandie = Provider("Normandie", "Farmer", "France", "A Normandy village")
        self.camembert_normand = cheese_provision(self.camembert, self.normandie)
    
    def test_provision_has_cheese(self):
        self.assertEqual("Camembert", self.camembert.name)
        
    def test_provision_has_provider(self):
        self.assertEqual("Farmer", self.normandie.type)
    
    def test_provision_has_no_id_yet(self):
        self.assertIsNone(self.camembert_normand.id)