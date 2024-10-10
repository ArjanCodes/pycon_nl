from oo_before import Promotion, Customer

def test_is_not_eligible_for_promotion():
    customer = Customer("Alice", 25)
    promotion = Promotion()
    assert not promotion.is_eligible(customer)

def test_is_eligible_for_promotion():
    customer = Customer("Alice", 55)
    promotion = Promotion()
    assert promotion.is_eligible(customer)