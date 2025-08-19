# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class App_Script(models.Model):

    #__App_Script_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__App_Script_FIELDS__END

    class Meta:
        verbose_name        = _("App_Script")
        verbose_name_plural = _("App_Script")


class App_Service(models.Model):

    #__App_Service_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__App_Service_FIELDS__END

    class Meta:
        verbose_name        = _("App_Service")
        verbose_name_plural = _("App_Service")


class Log_Entry(models.Model):

    #__Log_Entry_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    level = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)

    #__Log_Entry_FIELDS__END

    class Meta:
        verbose_name        = _("Log_Entry")
        verbose_name_plural = _("Log_Entry")



#__MODELS__END
