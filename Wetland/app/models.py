from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=true)
    password = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    register_time = models.DateTimeCheckMixin()

class Device(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    install_date = models.DateField(auto_now_add=true)
    install_time = models.TimeField(auto_now_add=true)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    project_name = models.CharField(max_length=50)

class Project(models.Model):
    name = models.CharField(max_length=50)
    num = models.UUIDField()
    owner = models.ForeignKey()


# Create your models here.
