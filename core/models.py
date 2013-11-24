from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Message(models.Model):
    object = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)

    def __unicode__(self):
        return "Obj: " + self.object + \
               " -  From: " + self.user.username + \
               " - In: " + self.project.title


class Feature(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    state = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name


class Transaction(models.Model):
    ADD_VALUE = 'add'
    SUPPORT_VALUE = 'support'

    TYPE = (
        (ADD_VALUE, 'Add Credit'),
        (SUPPORT_VALUE, 'Support'),
    )

    type = models.CharField(max_length=255, choices=TYPE, default='add')
    amount = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    feature = models.ForeignKey(Feature, null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user + "_" + self.type + "_" + self.amount


class UserDetail(models.Model):
    user = models.ForeignKey(User, unique=True)
    credits = models.IntegerField()

    def __unicode__(self):
        return self.user.username + "_details"
