from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.
class Register(models.Model):
  First_Name = models.CharField(max_length=300)
  Last_Name = models.CharField(max_length=300)
  Street = models.CharField(max_length=300)
  City = models.CharField(max_length=300)
  State = models.CharField(max_length=300)
  Country = models.CharField(max_length=300)
  Zip_Code = models.CharField(max_length=300)
  Phone_Number = models.CharField(max_length=300)
  Email = models.CharField(max_length=300)
  Date_of_Birth = models.CharField(max_length=300)
  Gender = models.CharField(max_length=300)
  Shirt_Size = models.CharField(max_length=300)
  Waiver = models.CharField(max_length=300)
  Emergency_Contact_First_Name = models.CharField(max_length=300)
  Emergency_Contact_Last_Name = models.CharField(max_length=300)
  Emergency_Contact_Phone_Number = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.Last_Name

class Donate(models.Model):
    # Your Information
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=300)

    # Credit Card Information
    cardholders_name = models.CharField(max_length=300)
    credit_card_number = models.CharField(max_length=300)
    card_cvv = models.CharField(max_length=300)
    expiration_date = models.CharField(max_length=300)

from django.contrib.auth.models import User

class Team(models.Model):
  name = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("team_detail", args=[self.id])