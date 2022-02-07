from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    user_name = models.CharField(db_column='User_Name', max_length=50)  # Field name made lowercase.
    user_id = models.IntegerField()
    pass_field = models.CharField(db_column='Pass', max_length=50)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login'
