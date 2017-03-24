from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
    payload  = models.CharField(max_length=1000)
    subject  = models.CharField(max_length=20)

    def __unicode__(self):
        return self.subject
