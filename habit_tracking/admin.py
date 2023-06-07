from django.contrib import admin
from .models import Habit, Day, HabitTracking

# Register your models here.
admin.site.register([Habit, Day, HabitTracking])