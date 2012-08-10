from django.db import models

class BaseMongo(object):

    def __init__(self, collection):
        self.coll = collection

    def __to_mongo__(self):
        return self.__to_mongo__()

    def get_collection(self):
        return self.coll


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


    def __to_mongo__(self):
        d = {'n': self.name, 'e': self.email, 'fbid': self.fbid, 'a': self.artistic}
        return d

    def save(self):
        self.collection.save(self.mobject)

    def __str__(self):
        return "name: %s; email: %s; artistic: %s;" % (self.name, self.email, self.artistic)
