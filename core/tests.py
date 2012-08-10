"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
#import unitttest
from models import Player
from nose.tools import assert_equal
from pymongo import Connection
from mockito import *

database_name = 'teamr_test'
host = 'localhost:27017'

class PlayerModelTest(TestCase):

    def setUp(self):
        self.conn = Connection(host)
        self.database = self.conn[database_name]
        self.collection = self.database['players']

    def test_save_ok(self):

        player = Player(self.collection, 'zezito', 'zezito@fclusitanos', 'idfb', 'o artista')

        expected = player.mobject
        import ipdb;ipdb.set_trace()
        player.save()
        actual = self.collection.find_one({'e': player.email})
        assert_equal(actual, expected)

    def tearDown(self):
        self.conn.drop_database(database_name)

#class ModelsTest(TestCase)
#
#
#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)



