# encoding:utf8
from django.db import models


# 用户
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    register_time = models.DateTimeField(auto_now=True)

# 项目，默认一个
class Project(models.Model):
    name = models.CharField(max_length=50)
    num = models.UUIDField()
    create_time = models.DateTimeField(auto_now_add=True)

# 设备类型
class DeviceType(models.Model):
    num = models.IntegerField(default=0)
    type_name = models.CharField(max_length=50)
    type_num = models.IntegerField(default=0) # 该类型设备数量

# 设备，区分不同类型设备、归属不同的项目
class Device(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    device_type = models.ForeignKey(DeviceType, related_name="device", null=True)
    address = models.CharField(max_length=50)
    install_date = models.DateField(auto_now_add=True)
    install_time = models.TimeField(auto_now_add=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    project_name = models.CharField(max_length=50)
    project_id = models.ForeignKey(Project, related_name="device", null=True)
    owner_id = models.ForeignKey(User, related_name="device", null=True)

# 异常事件类型MAP
class AbnormalEventType(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=50)

# 异常事件
class AbnormalEvent(models.Model):
    num = models.UUIDField()
    event_type = models.ForeignKey(AbnormalEventType, related_name="abnormalEvent", null=True)
    name = models.CharField(max_length=50)
    device_id = models.ForeignKey(Device, related_name="abnormalEvent", null=True)
    project_id = models.ForeignKey(Project, related_name="abnormalEvent", null=True)
    content = models.CharField(max_length=500)


# 采集数据
class Data(models.Model):
    device_num = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)
    content = models.TextField()
    device_id = models.ForeignKey(Device, related_name="data", null=True)

# Create your models here.
