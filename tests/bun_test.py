import pytest
from bun import Bun



class TestBun:
    @pytest.mark.parametrize('name', ["Bun",None])
    def test_init_bun_name(self, name):
        price = 1.5
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [1.5, None])
    def test_init_bun_price(self, price):
        name = 'Bun'
        bun = Bun(name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("name, price", [("name", 224), ("Имя", 213.13)])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [("name", 224), ("Имя", 213.13)])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price