from django.db import models


class Lamp(models.Model):
	name = models.CharField(max_length=200)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-id',)

class Schedule(models.Model):
	lamp = models.ForeignKey(Lamp, related_name="schedules")
	lamp_date = models.DateField()
	lamp_time = models.TimeField()
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.lamp.name


class Log(models.Model):
	schedule = models.ForeignKey(Schedule, related_name="logs")
	log_date = models.DateField(auto_now_add=True)
	log_time = models.TimeField(auto_now_add=True)

	def __str__(self):
		return self.schedule.lamp.name


# Signal life
from django.db.models.signals import post_save


def when_schedule_add_or_update(sender, instance, created, **kwargs):
	Log.objects.create(schedule=instance)

post_save.connect(when_schedule_add_or_update, sender=Schedule)