from django.db import models


class Org(models.Model):
    team_id      = models.CharField(max_length=256, primary_key=True)
    team_pre     = models.IntegerField(default=0)
    team_aft     = models.IntegerField(default=0)
    """
    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id_team)])
    
    def __str__(self):
        return self.team_id
    """

class User(models.Model):
    # Orgクラスから外部キーを参照する
    org          = models.ForeignKey("Org", to_field='team_id', on_delete=models.SET_NULL, null=True)
    display_name = models.CharField(max_length=256, null=True)
    student_id   = models.CharField(max_length=256, primary_key=True)
    qtr_pre      = models.IntegerField(default=0) # 前期講義日程
    qtr_aft      = models.IntegerField(default=0) # 後期講義日程
    
    """
    def get_absolute_url(self):
        return reverse('member-detail', args=[str(self.student_id)])
    
    def __str__(self):
        return self.org
    """



