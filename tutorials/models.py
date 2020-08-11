from django.db import models


class Carehome(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Deaths = models.IntegerField()

class WeeklyCarehome(models.Model):
    Week = models.DateField(auto_now=False, auto_now_add=False)
    total = models.IntegerField()
    covid = models.IntegerField()
    t2018 = models.FloatField()
    t2017 = models.FloatField()
    t2016 = models.FloatField()
    t2015 = models.FloatField()

