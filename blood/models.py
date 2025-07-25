from django.db import models

class Donor(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=30)  
    gender = models.CharField(max_length=10, default='Other')  
    blood_group = models.CharField(max_length=3)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    last_donation = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

class PatientRequest(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.blood_group}"

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
