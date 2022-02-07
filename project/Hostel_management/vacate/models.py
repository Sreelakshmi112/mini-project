from django.db import models

# Create your models here.
class Vacate(models.Model):
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    s_id = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vacate'
