from django.db import models

from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from datetime import*

class UserAdmin(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="useradmin", null=True, blank=True)
    droit = models.CharField(max_length=20, choices=(
    		('super-user', 'super-user'),
    	))

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return '{}'.format(self.user.username)