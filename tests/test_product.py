def test_product_init(product):
    assert product.name == "AirPods"
    assert product.description == "white"
    assert product.price == 35000.0
    assert product.quantity == 3
