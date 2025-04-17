from script.deploy import deploy_favorites 

def test_starting_vale():
    favorites_contract = deploy_favorites()
    print(favorites_contract.retrieve())
    assert favorites_contract.retrieve() == 88


def test_can_change_values():
    favorites_contract = deploy_favorites()
    favorites_contract.store(66)
    assert favorites_contract.retrieve() == 66
