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
    TYPE = (
        (0, 'Add Credit'),
        (1, 'Support'),
    )

    type = models.TextField(choices=TYPE)
    amount = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    feature = models.ForeignKey(Feature, null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user + "_" + self.type + "_" + self.amount
