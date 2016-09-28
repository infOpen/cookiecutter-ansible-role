"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)

def test_foo_a(User):
    assert User().name == 'root'

def test_foo_b(User):
    assert User().name == 'root'
