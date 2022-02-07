from django.db import models
from stu_register.models import StuRegister
# Create your models here.

class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(StuRegister,to_field='id',on_delete=models.CASCADE)
    complaint = models.CharField(max_length=70)
    reply = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'complaint'

