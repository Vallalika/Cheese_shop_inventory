import unittest
from models.cheese import Cheese

class TestCheese(unittest.TestCase):
    
    def setUp(self):
        self.camembert = Cheese("Camembert", "France", "Raw Cow's Milk", "Fine velvety rind marked by brown-red streaks. Light yellow interior. Supple texture. Aromas of forest floor, mushroom and earth after ripening. Milky and tart notes.", 20, 5.00, 8.00)
    
    
    def test_cheese_has_name(self):
        self.assertEqual("Camembert", self.camembert.name)
        
    def test_cheese_has_origin(self):
        self.assertEqual("France", self.camembert.origin)
        
    def test_cheese_has_description(self):
        self.assertEqual("Fine velvety rind marked by brown-red streaks. Light yellow interior. Supple texture. Aromas of forest floor, mushroom and earth after ripening. Milky and tart notes.", self.camembert.description)
    
    def test_cheese_has_stock(self):
        self.assertEqual(20, self.camembert.stock)
    
    def test_cheese_has_buying_cost(self):
        self.assertEqual(5.00, self.camembert.buying_cost)

    def test_cheese_has_selling_price(self):
        self.assertEqual(8.00, self.camembert.selling_price)
        
    def test_cheese_has_no_provider(self):
        self.assertIsNone(self.camembert.providers)
    
    def test_cheese_has_no_id_yet(self):
        self.assertIsNone(self.camembert.id)