from django.shortcuts import render
from .models import schedule

def sch(request):

    sch = schedule.objects.all()
    args = {'sch': sch}
    return render(request, "sch.html", args)
