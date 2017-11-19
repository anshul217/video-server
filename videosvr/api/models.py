from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class User(AbstractUser):
    phone = models.CharField(_('phone number'),
                             max_length=15,
                             help_text=_('Enter phone number')
                             )
    is_verified = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
  