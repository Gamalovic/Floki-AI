from django.urls import path
from schedule import views

urlpatterns = [
    path('sch', views.sch, name="schedule"),
    



]
