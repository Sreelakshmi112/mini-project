from django.db import models

# Create your models here.
#
# class Attendance(models.Model):
#     working_days = models.IntegerField(db_column='Working_days')  # Field name made lowercase.
#     attendance = models.IntegerField(db_column='Attendance')  # Field name made lowercase.
#     student_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'attendance'
#
class Attendance(models.Model):
    month = models.CharField(db_column='Month', max_length=60)  # Field name made lowercase.
    working_days = models.IntegerField(db_column='Working_days')  # Field name made lowercase.
    attendance = models.IntegerField(db_column='Attendance')  # Field name made lowercase.
    student_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance'
