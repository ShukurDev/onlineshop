from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps


# Create your models here.


class BaseUser(AbstractUser):
    age = models.IntegerField(verbose_name='age', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if f"{self.first_name} {self.last_name}" else (
                self.username or self.email)
# 1-problem

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         Profile.objects.create(
    #             user=self.username,
    #             name=self.last_name,
    #         )
    #     super(BaseUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    GENDER = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    user = models.OneToOneField(BaseUser, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=True)
    photo = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, null=True, max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
# 2- problem

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        if not self.id:
            Cart = apps.get_model('card', 'Cart')
            Cart.objects.create(
                profile=self.user,
            )
        super(Profile, self).save(*args, **kwargs)


class Address(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user_address')
    # country = models.CharField(max_length=130, null=True, blank=True)
    REGION = {
        ('Toshkent', 'Toshkent:'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Andijon', 'Andijon'),
        ('Namangan', 'Namangan'),
        ('Navoi', 'Navoi'),
        ('Samarqand', 'Samarqand'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Xorazm', 'Xorazm'),
        ('Fargona', 'Fargona'),
        ('Jizzax', 'Jizzax'),
        ('Toshkent vil', 'Toshkent vil'),
        ('Buxoro', 'Buxoro'),
    }
    region = models.CharField(max_length=100, choices=REGION, default='empty')
    city = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=300, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.region
