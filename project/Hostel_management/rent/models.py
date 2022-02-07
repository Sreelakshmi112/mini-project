from django.db import models

# Create your models here.

class Rent(models.Model):
    days = models.CharField(db_column='Days', max_length=50)  # Field name made lowercase.
    fees = models.IntegerField(db_column='Fees')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rent'

