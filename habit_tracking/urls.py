from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('', views.main_page)
]