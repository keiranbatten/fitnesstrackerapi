from django.db import models
import datetime

class Total(models.Model):
    date = models.DateField(blank=False, default=datetime.date.today, unique=True)
    kilojoules = models.FloatField(blank=False, default=0)
    carbohydrates = models.FloatField(blank=False, default=0)
    fat = models.FloatField(blank=False, default=0)
    protein = models.FloatField(blank=False, default=0)
    sodium = models.FloatField(blank=False, default=0)
    sugar = models.FloatField(blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meal(models.Model):
    date = models.DateField(blank=False, default=datetime.date.today)
    type = models.TextField(blank=False)
    kilojoules = models.FloatField(blank=False, default=0)
    carbohydrates = models.FloatField(blank=False, default=0)
    fat = models.FloatField(blank=False, default=0)
    protein = models.FloatField(blank=False, default=0)
    sodium = models.FloatField(blank=False, default=0)
    sugar = models.FloatField(blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)