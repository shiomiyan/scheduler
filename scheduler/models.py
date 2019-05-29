from django.db import models

class class_id(models.Model):
    user_data = models.IntegerField(default=0)
    name= models.CharField(max_length=256)
    team_id = models.CharField(max_length=256)

class class_ps(models.Model):
    team_id2 = models.CharField(max_length=256)
    share_data =models.IntegerField(default=0)





