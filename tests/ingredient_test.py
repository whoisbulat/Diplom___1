from ingredient import Ingredient



class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient("Соус", "Сальса", 0.5)
        assert ingredient.get_name() == "Сальса"

    def test_get_price(self):
        ingredient = Ingredient("Соус", "Сальса", 0.5)
        assert ingredient.get_price() == 0.5

    def test_get_type(self):
        ingredient = Ingredient("Соус", "Сальса", 0.5)
        assert ingredient.get_type() == "Соус"