from django.db import models
from rest_framework import serializers
from MFP.models import Total, Meal

class TotalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Total
        fields = ('id',
                'date',
                'kilojoules',
                'carbohydrates',
                'fat',
                'protein',
                'sodium',
                'sugar')

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id',
                'date',
                'type',
                'kilojoules',
                'carbohydrates',
                'fat',
                'protein',
                'sodium',
                'sugar')