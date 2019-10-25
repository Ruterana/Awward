from django.test import TestCase

# Create your tests here.
from django.test import TestCase
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.charlene= Editor(bio = 'software developer')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.charlene,Profile))
