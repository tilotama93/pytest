import pytest

@pytest.mark.smoke
def test_login():
    print('login Done')

@pytest.mark.regression
def test_addproduct():
    print('add product')

@pytest.mark.smoke
def test_logout():
    print('logout Done')
