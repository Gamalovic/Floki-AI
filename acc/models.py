from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    stu_y = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),)

    year = models.IntegerField(choices=stu_y, null=True, blank=True)

    description = models.TextField(default='write something about yourself ...', max_length=500)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
