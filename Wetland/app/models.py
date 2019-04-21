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
    value = models.FloatField(default=0.0, null=True)

# 异常事件
class AbnormalEvent(models.Model):
    num = models.UUIDField()
    event_type = models.ForeignKey(AbnormalEventType, related_name="abnormalEvent", null=True)
    name = models.CharField(max_length=50)
    device_id = models.ForeignKey(Device, related_name="abnormalEvent", null=True)
    project_id = models.ForeignKey(Project, related_name="abnormalEvent", null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True, null=True)
    content = models.CharField(max_length=500)

# 采集数据
class Data(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True)
    content = models.TextField()
    device_id = models.ForeignKey(Device, related_name="data", null=True)

#视频图像
class videoImage(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True)
    img_src = models.TextField()
    device_num = models.CharField(max_length=500)

#气象站数据
class meteorologyData(models.Model):
    windySpeed = models.FloatField(null=True) # 风速
    windyDirection = models.IntegerField(null=True) #风向
    temperature = models.FloatField(null=True) # 摄氏度
    humidity = models.FloatField(null=True) #湿度(0-100)
    noise = models.FloatField(null=True) #噪声(0-150db)
    pressure = models.FloatField(null=True) #气压 (kpa)
    light = models.FloatField(null=True) #光照
    rainy = models.FloatField(null=True) #雨量 (mm)
    create_date = models.DateField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True, null=True)

#空气质量监测数据
class airData(models.Model):
    windySpeed = models.FloatField(null=True) # 风速
    windyDirection = models.IntegerField(null=True) #风向
    pm25 = models.FloatField(null=True) # Pm2.5
    pm10 = models.FloatField(null=True) # pm10
    o3 = models.FloatField(null=True) # O3
    co = models.FloatField(null=True) # Co
    so2 = models.FloatField(null=True) # SO2
    no2 = models.FloatField(null=True) # NO2
    temperature = models.FloatField(null=True) # 摄氏度
    humidity = models.FloatField(null=True) #湿度(0-100)
    create_date = models.DateField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True, null=True)


#水文水质数据
class waterData(models.Model):
    waterLevel = models.FloatField(null=True) # 水位
    o3 = models.FloatField(null=True) # 溶解氧
    temperature = models.FloatField(null=True) # 摄氏度
    elec = models.FloatField(null=True) # 氧化还原电位
    conductivity = models.FloatField(null=True) # 电导率
    ph = models.FloatField(null=True) # Ph值
    transparency = models.FloatField(null=True) # 透明度
    waterSpeed = models.FloatField(null=True) # 流速
    nh4 = models.FloatField(null=True) # NH4
    create_date = models.DateField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True, null=True)


#土壤数据
class soilData(models.Model):
    temperature = models.FloatField(null=True) # 摄氏度
    humidity = models.FloatField(null=True) #湿度(0-100)
    conductivity = models.FloatField(null=True) # 电导率
    ph = models.FloatField(null=True) # Ph值
    create_date = models.DateField(auto_now_add=True, null=True)
    create_time = models.TimeField(auto_now_add=True, null=True)
    

# Create your models here.
