from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BaseUser(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(verbose_name='age', null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name if self.full_name else self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    GENDER = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    user = models.OneToOneField(BaseUser, related_name='user', on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, null=True, max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


class Address(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user_address')
    country = models.CharField(max_length=130, null=True, blank=True)
    # REGION = {
    #     ('Toshkent', 'Toshkent'),
    #     ('Surxondaryo', 'Surxondaryo'),
    #     ('Andijon', 'Andijon'),
    #     ('Namangan', 'Namangan'),
    # }
    #
    region = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=300, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_address.username} - {self.address}"
