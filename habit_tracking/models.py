from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=50)
    creationdate = models.DateField(auto_now_add=True) 
    # maybe change this so that we can create with other date for testing (see documentation)
    frequency_goal = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)]) 
    # habits are minimum once per week for other tasks cretate another feature like reminders
    colour = models.CharField(max_length=7) 
    # maybe add a regex valication so only valid colours are allowed
    
    # maybe a description
    
    def __str__(self):
        return self.name


class Day(models.Model):
    date = models.DateField()
    
    # maybe day of the week
    
    def __str__(self):
        return self.date


class HabitTracking(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.ForeignKey(Day, on_delete=models.CASCADE)
    # maybe not delete the data if the habit is deleted so that we can look at statistics later
    amount = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)]) # jennita
    # probably impractical to do a habit more that five times a day (plus don't know how to do it in ui yet)
    # maybe work with percentages or add a field for goal of this day (because the goal might change)
    
    def __str__(self):
        return f'{self.date}, {self.date}'
