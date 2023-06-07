from django.shortcuts import render
from .models import Habit

# Create your views here.
def main_page(request):
    habits = Habit.objects.all()  # Retrieve habit data from the database
    context = {'habits': habits}  # Create the template context 
    return render(request, 'main_page.html', context)  # Render the template with the context
