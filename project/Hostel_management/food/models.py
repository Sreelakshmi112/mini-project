from django.db import models

# Create your models here.

# class Food(models.Model):
#     day = models.CharField(db_column='Day', max_length=50)  # Field name made lowercase.
#     food_time = models.CharField(db_column='Food time', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     food_items = models.CharField(db_column='Food items', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = False
#         db_table = 'food'
class Food(models.Model):
    day = models.CharField(db_column='Day', max_length=50)  # Field name made lowercase.
    breakfast = models.CharField(db_column='BREAKFAST', max_length=100)  # Field name made lowercase.
    lunch = models.CharField(db_column='LUNCH', max_length=100)  # Field name made lowercase.
    dinner = models.CharField(db_column='DINNER', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food'

