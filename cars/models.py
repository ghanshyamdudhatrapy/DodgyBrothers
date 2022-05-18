from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

CAR_CONDITION_CHOICE = [
    ("poor", "Poor"),
    ("fair", "Fair"),
    ("good", "Good"),
    ("excellent", "Excellent"),
]


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        usr_exist = User.objects.filter(email=email)
        if len(usr_exist) >= 1:
            return usr_exist.first()
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.username = email
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('username', email)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

class Cars(models.Model):
    seller_name = models.CharField(max_length=100, blank=False, null=False)
    seller_mob = models.CharField(max_length=100, blank=False, null=False)
    make = models.CharField(max_length=100, blank=False, null=False)
    model = models.CharField(max_length=100, blank=False, null=False)
    year = models.DateField()
    condition = models.CharField(
        max_length=100, choices=CAR_CONDITION_CHOICE, default="processing")
    price = models.IntegerField(
        validators=[MaxValueValidator(100000), MinValueValidator(1000)])
    is_sell = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ('-id',)
