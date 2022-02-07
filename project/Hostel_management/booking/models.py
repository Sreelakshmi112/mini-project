from django.db import models
from stu_register.models import StuRegister
# class Booking(models.Model):
#     date = models.DateField()
#     # s_id = models.IntegerField()
#     s= models.ForeignKey(StuRegister, to_field='id', on_delete=models.CASCADE)
#     status = models.CharField(max_length=50)
#     r_id = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'booking'

class Booking(models.Model):
    date = models.DateField()
    # s_id = models.IntegerField()
    s = models.ForeignKey(StuRegister, to_field='id', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    r_id = models.IntegerField()
    no_of_days = models.IntegerField(db_column='No.of days', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_of_room = models.IntegerField(db_column='No.of room', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'



