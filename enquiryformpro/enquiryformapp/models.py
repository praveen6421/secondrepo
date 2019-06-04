from django.db import models

class EnquiryFormData(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile = models.BigIntegerField()
    qualification = models.CharField(max_length=20)
    location = models.CharField(max_length=20)