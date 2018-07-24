from django.db import models

class schedule(models.Model):
    # subject_name = models.CharField(max_length=30)
    # date = models.DateField() ##the day ex : sunday ,monday , ..etc
    # start_time = models.TimeField() 
    # end_time = models.TimeField()
    # instructor_name = models.CharField(max_length=30)
    # subject_grade = models.IntegerField()

    d = (
        ('SUN', 'sunday'),
        ('MON', 'monday'),
        ('TUE', 'tuesday'),
        ('WED', 'wednssday'),
        ('THU', 'thursday'),)
    subject_name = models.CharField(max_length=30)
    day = models.CharField(max_length=3, choices=d)  # the day ex : sunday ,monday , ..etc
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor_name = models.CharField(max_length=30)
    subject_grade = models.IntegerField()