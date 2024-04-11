from Testy.classProduct.product import Product

class TestCaseProduct():
    def test_generate_sku(self):

        exp_generate_sku = "BUTY-14-ZIELONE"
        buty = Product("buty",14, "zielone")
        actual_value = buty.generate_sku()
        assert actual_value==exp_generate_sku


