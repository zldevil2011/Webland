from django.contrib import admin

from models import User, Device, Project, DeviceType, AbnormalEvent, AbnormalEventType, Data

class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'register_time')

class DeviceAdmin(admin.ModelAdmin):
  list_display = ('num', 'install_date', 'latitude', 'latitude', 'owner_id')

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'num', 'create_time')

class DeviceTypeAdmin(admin.ModelAdmin):
  list_display = ('type_name', 'num', 'type_num')

admin.site.register(User, UserAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(AbnormalEvent)
admin.site.register(AbnormalEventType)
admin.site.register(Data)

# Register your models here.
