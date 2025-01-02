def test_category_init(first_category, second_category):
    assert first_category.name == "Наушники"
    assert first_category.description == "Современные беспроводные наушники"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4
