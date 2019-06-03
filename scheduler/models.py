from django.db import models

class User(models.Model):
    student_id = models.CharField(max_length=256,primary_key=True)
    q_pre = models.IntegerField(default=0)
    q_aft = models.IntegerField(default=0)
    name= models.CharField(max_length=256,null=True)
    
    #外部キー
    team = models.ForeignKey('Org', to_field='team_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    """
    def get_absolute_url(self):
        return reverse('member-detail', args=[str(self.student_id)])
    """

class Org(models.Model):
    team_id = models.CharField(max_length=256,primary_key=True)
    name =  models.CharField(max_length=30)
    share_pre =models.IntegerField(default=0)
    share_aft =models.IntegerField(default=0)
    
    """
    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id_team)])
    """
    def __str__(self):
        return f'{self.name}'





