from django.db import models

# Create your models here.
class Rolde(models.Model):
    Role_ID = models.IntegerField()
    Role_Name = models.CharField(max_length=50)


class Division(models.Model):
    Division_ID = models.AutoField(primary_key=True,null=False)
    Division_Name = models.CharField(max_length=50)

class District(models.Model):
    District_ID = models.AutoField(primary_key=True, null=False)
    Division_ID = models.ForeignKey(Division, on_delete=models.CASCADE)
    District_Code = models.IntegerField(null=True)
    District_Name = models.IntegerField(null=True)
    District_Latitude = models.FloatField(null=True)
    Distric_Longitude = models.FloatField(null=True)



class College(models.Model):
    College_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=50)


