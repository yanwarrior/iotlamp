from django.contrib import admin
from .models import Lamp, Schedule, Log


# Register your models here.
class LampAdmin(admin.ModelAdmin):
	list_display = ['name', 'status']


class ScheduleAdmin(admin.ModelAdmin):
	list_display = ['lamp', 'lamp_date', 'lamp_time', 'status']


class LogAdmin(admin.ModelAdmin):
	list_display = ['schedule', 'log_date', 'log_time']


admin.site.register(Lamp, LampAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Log, LogAdmin)