from django.db import models

class User_test(models.Model):
    
        username = models.CharField(max_length=100)
        mail = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
