from unittest.mock import Mock
from burger import Burger


class TestBurger:
    def test_set_buns_should_set_bun_correctly(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булка'
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient_should_append_to_ingredients_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Помидор"
        mock_ingredient.get_type.return_value = "Овощь"
        mock_ingredient.get_weight.return_value = 100
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients


    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Тост"
        mock_ingredient.get_type.return_value = "мучное"
        mock_ingredient.get_weight.return_value = 100
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients


    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Тост"
        mock_ingredient1.get_type.return_value = "мучное"
        mock_ingredient1.get_weight.return_value = 100
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Тост"
        mock_ingredient2.get_type.return_value = "мучное"
        mock_ingredient2.get_weight.return_value = 100
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булка'
        mock_bun.get_price.return_value = 100
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Тост"
        mock_ingredient1.get_type.return_value = "мучное"
        mock_ingredient1.get_weight.return_value = 100
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Тост"
        mock_ingredient2.get_type.return_value = "мучное"
        mock_ingredient2.get_weight.return_value = 100
        mock_ingredient2.get_price.return_value = 75
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = mock_bun.get_price() * 2 + mock_ingredient1.get_price() + mock_ingredient2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булка'
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Тост"
        mock_ingredient1.get_type.return_value = "мучное"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Котлета"
        mock_ingredient2.get_type.return_value = "мясо"
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.get_price = Mock(return_value=300)

        expected_receipt = "(==== Булка ====)\n= мучное Тост =\n= мясо Котлета =\n(==== Булка ====)\n\nPrice: 300"
        assert burger.get_receipt() == expected_receipt