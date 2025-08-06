from tortoise import fields
from tortoise.models import Model

class Users(Model):
    fullname = fields.CharField(max_length=100)
    age = fields.IntField()
    email = fields.CharField(max_length=100,)
    password = fields.CharField(max_length=100)

    def __str__(self):
        return self.fullname