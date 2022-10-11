import pytest
import sys


@pytest.mark.skip
def test_login():
    print('login Done')

@pytest.mark.skipif(sys.system.version<(3,9),reson='python is not supported')
def test_addproduct():
    print('add product')

@pytest.mark.smoke
def test_logout():
    print('logout Done')


