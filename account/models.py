from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices =(('M', 'Male'), ('F','Female')), blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    updated      = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
# Create your models here.
