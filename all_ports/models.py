from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Member(models.Model):
  # Boat specifiaction
  boatLenght = models.PositiveIntegerField()
  boatWidth = models.PositiveIntegerField()
  boatDeep = models.PositiveIntegerField()

  # Person specification - name, phone, so on
  firstName = models.CharField(max_length=255)
  secondName = models.CharField(max_length=255)
  phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)

