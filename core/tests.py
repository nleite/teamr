"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
#import unitttest
from models import Player
from nose.tools import assert_equal, assert_not_equal
from pymongo import Connection
from mockito import *

database_name = 'teamr_test'
host = 'localhost:27017'

class PlayerModelTest(TestCase):

    def setUp(self):
        self.conn = Connection(host)
        self.database = self.conn[database_name]
        self.collection = self.database['players']
        self.email = 'player@email.com'
        self.name = 'player'
        self.fbid = 'fbid'
        self.artist = 'artist'

    def testSaveOkCheckArtist(self):

        player = Player(self.collection, self.name, self.email, self.fbid, self.artist)
        expected = player.mobject
        #import ipdb;ipdb.set_trace()
        player.save()
        actual = self.collection.find_one({'e': player.email})
        assert_equal(actual['a'], expected['a'])

    def testSaveOkCheckEmail(self):
        player = Player(self.collection, self.name, self.email, self.fbid, self.artist)
        expected = self.email
        player.save()
        q = {'e': self.email}
        actual = self.collection.find_one(q)['e']
        assert_equal(expected, actual)

    def testLoadExistingPlayer(self):
        obj = {'a': self.artist, 'e': self.email, 'fbid': self.fbid, 'n': self.name}
        self.collection.save(obj)
        player = Player.load(self.collection, self.email)

        assert_not_equal(None, player)

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



