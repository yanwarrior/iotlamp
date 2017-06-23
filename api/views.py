from rest_framework import generics
from iot.models import Lamp, Schedule, Log
from .serializers import LampSerializer, ScheduleSerializer, LogSerializer


class LampList(generics.ListCreateAPIView):
	queryset = Lamp.objects.all()
	serializer_class = LampSerializer


class LampDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Lamp.objects.all()
	serializer_class = LampSerializer


class ScheduleList(generics.ListCreateAPIView):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer


class LogList(generics.ListCreateAPIView):
	queryset = Log.objects.all()
	serializer_class = LogSerializer


class LogDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Log.objects.all()
	serializer_class = LogSerializer