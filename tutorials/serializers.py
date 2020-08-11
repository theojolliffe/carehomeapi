from rest_framework import serializers 
from tutorials.models import Carehome
from tutorials.models import WeeklyCarehome
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Carehome
        fields = ('id',
                  'Date',
                  'Deaths')


class WeeklyCarehomeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = WeeklyCarehome
        fields = ('id',
                  'Week',
                  'total',
                  'covid',
                  't2018',
                  't2017',
                  't2016',
                  't2015')
