from django.db import models

# Create your models here.
class Application(models.Model):
    Name=models.CharField(max_length=100)
    DOB=models.DateField()
    Age=models.CharField(max_length=3)
    Gender=models.CharField(max_length=20)
    PhNo=models.CharField(max_length=12 )
    District=models.CharField(max_length=10)
    Branch=models.CharField(max_length=10)
    Account=models.CharField(max_length=50)
    Materials=models.CharField(max_length=50)



