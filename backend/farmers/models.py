import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

SEX_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class RegistrationCode(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=20)
    
    def __str__(self):
        return f"{self.email} - {self.code}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
class Cell(models.Model):
    cell_id = models.PositiveIntegerField()
    country = models.CharField(max_length=200)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    cellule_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('cell_id', 'country', 'province', 'district', 'sector', 'cellule_name')

    def __str__(self):
        return f"#{self.country} ~ {self.cellule_name} - {self.sector}, {self.district}, {self.province}"

class Village(models.Model):
    cell = models.ForeignKey("Cell", on_delete=models.CASCADE, related_name='villages')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (in {self.cell})"


class Farmer(models.Model):
    full_name = models.CharField(max_length=200)
    national_id = models.CharField(max_length=22, unique=True, db_index=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone_number = models.CharField(max_length=20)
    location = models.ForeignKey("Village", on_delete=models.SET_NULL, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Species(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class SeedDistribution(models.Model):
    farmer = models.ForeignKey("Farmer", on_delete=models.CASCADE, related_name="distributions")
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    distributed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer.full_name} - {self.species.name} ({self.quantity})"
