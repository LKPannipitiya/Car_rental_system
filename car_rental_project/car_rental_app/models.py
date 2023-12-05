from django.db import models


class SignupData(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    license_number = models.CharField(max_length=50)
    license_exp = models.DateField()
    payment_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

