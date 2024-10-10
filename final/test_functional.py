from functional import is_eligible_for_promotion, Customer

def test_is_not_eligible_for_promotion():
    customer = Customer("Alice", 25)
    assert not is_eligible_for_promotion(customer)
    

def test_is_eligible_for_promotion():
    customer = Customer("Alice", 55)
    assert is_eligible_for_promotion(customer)