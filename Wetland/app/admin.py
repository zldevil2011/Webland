from django.contrib import admin

from models import User, Device, Project, DeviceType, AbnormalEvent, AbnormalEventType, Data

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Project)
admin.site.register(DeviceType)
admin.site.register(AbnormalEvent)
admin.site.register(AbnormalEventType)
admin.site.register(Data)

# Register your models here.
