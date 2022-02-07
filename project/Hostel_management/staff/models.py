from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_name = models.CharField(db_column='Staff_name', max_length=50)  # Field name made lowercase.
    phone_no = models.IntegerField(db_column='Phone_no')  # Field name made lowercase.
    job_type = models.CharField(db_column='Job_type', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'
