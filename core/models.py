from django.db import models

class BaseMongo(object):

    def __init__(self, collection):
        self.coll = collection

    def __to_mongo__(self):
        return self.__to_mongo__()

    def get_collection(self):
        return self.coll

    @classmethod
    def load(cls, collection, id):
        return cls.__from_mongo__(collection, id)

    collection = property(get_collection)


    mobject = property(__to_mongo__)

# Create your models here.
class Player(BaseMongo):


    def __init__(self, collection, name, email, fbid, artistic):
        BaseMongo.__init__(self, collection)
        self.name = name
        self.email = email
        self.fbid = fbid
        self.artistic = artistic


    @classmethod
    def __from_mongo__(cls, collection, email):
        """
        Returns a single Player object identified by email"""
        #query object
        query = {'e': email}
        obj = collection.find_one(query)
        if obj is not None:
            return Player(collection, obj['n'], email, obj['fbid'], obj['a'])
        return None

    def __to_mongo__(self):
        """
        Parses Player instance into a dictonary so it can be inserted into mongo collection"""
        d = {'n': self.name, 'e': self.email, 'fbid': self.fbid, 'a': self.artistic}
        return d

#    def load(collection, email):
#        return Player.__from_mongo__(collection, email)

    def save(self):
        self.collection.save(self.mobject)

    def __str__(self):
        return "name: %s; email: %s; artistic: %s;" % (self.name, self.email, self.artistic)
