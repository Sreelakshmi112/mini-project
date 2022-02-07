from django.db import models

# Create your models here.

class Room(models.Model):
    available_rm = models.IntegerField(db_column='Available_rm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


