from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.db import models

ACTIVITY_CHOICES = (
(0, '--Select--'),
(1, 'Promote event'),
(2, 'Set Up'),
(3, 'Service hikers'),
)
# Create your models here.
class Register(models.Model):
  Street = models.CharField(max_length=300)
  City = models.CharField(max_length=300)
  State = models.CharField(max_length=300)
  Country = models.CharField(max_length=300)
  Zip_Code = models.CharField(max_length=300)
  Phone_Number = models.CharField(max_length=300)
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

class Member(models.Model):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

class Vendor(models.Model):
  First_Name = models.CharField(max_length=300)
  Last_Name = models.CharField(max_length=300)
  Street = models.CharField(max_length=300)
  City = models.CharField(max_length=300)
  State = models.CharField(max_length=300)
  Country = models.CharField(max_length=300)
  Zip_Code = models.CharField(max_length=300)
  Phone_Number = models.CharField(max_length=300)
  Email = models.CharField(max_length=300)
 
class Volunteer(models.Model):
  First_Name = models.CharField(max_length=300)
  Last_Name = models.CharField(max_length=300)
  Street = models.CharField(max_length=300)
  City = models.CharField(max_length=300)
  State = models.CharField(max_length=300)
  Country = models.CharField(max_length=300)
  Zip_Code = models.CharField(max_length=300)
  Phone_Number = models.CharField(max_length=300)
  Email = models.CharField(max_length=300)
  Activity = models.IntegerField(choices=ACTIVITY_CHOICES, default=0)

class Contact_Us(models.Model):
  name = models.CharField(max_length=70)
  email = models.EmailField(max_length=70)
  phone_number = models.CharField(max_length=11)
  topic = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

class RegisterWaiver(models.Model):
  waiver = models.BooleanField(verbose_name='I hereby accept the waiver.')
  