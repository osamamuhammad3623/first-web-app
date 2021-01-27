from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class password(models.Model):
    genPass = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, related_name='cpg_user')

    def __str__(self):
        return self.genPass