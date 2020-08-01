from django.db import models


# Create your models here.
class Polls(models.Model):
    poll_name = models.CharField(max_length=50)
    poll_description = models.CharField(max_length=200)

    @classmethod
    def createpoll(cls, poll_name, poll_description):
        return cls(poll_name=poll_name, poll_description=poll_description)

    class Meta:
        db_table = 'Polls'


class UserProfile(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16)

    @classmethod
    def createuser(cls, username, password):
        return cls(username=username, password=password)

    class Meta:
        db_table = 'UserProfiles'
