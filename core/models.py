from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Register(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title