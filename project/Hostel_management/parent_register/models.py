from django.db import models

# Create your models here.

class ParentRegister(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)  # Field name made lowercase.
    phone_no = models.IntegerField(db_column='Phone_no')  # Field name made lowercase.
    s_id = models.IntegerField()
    city = models.CharField(db_column='CITY', max_length=50)  # Field name made lowercase.
    pincode = models.IntegerField()
    e_mail = models.CharField(db_column='E-mail', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parent_register'

