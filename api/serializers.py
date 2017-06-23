from rest_framework import serializers
from iot.models import Lamp, Schedule, Log


class LogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Log
		fields = ('id', 'schedule', 'log_date', 'log_time')


class ScheduleSerializer(serializers.ModelSerializer):
	logs = LogSerializer(many=True, read_only=True, required=False)

	class Meta:
		model = Schedule
		fields = ('id', 'lamp', 'lamp_date', 'lamp_time', 'status', 'logs')


class LampSerializer(serializers.ModelSerializer):
	schedules = ScheduleSerializer(many=True, read_only=True, required=False)

	class Meta:
		model = Lamp
		fields = ('id', 'name', 'status', 'schedules')



