from django.db import models

# Create your models here.

class StuRegister(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    gender = models.CharField(max_length=30)
    department = models.CharField(db_column='Department', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    student_phno = models.IntegerField(db_column='Student_phno')  # Field name made lowercase.
    parent_id = models.IntegerField()
    e_mail = models.CharField(db_column='E-mail', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stu_register'


