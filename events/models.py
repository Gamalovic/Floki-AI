from django.db import models


class Event(models.Model):
    event_year = (
        (1, 'First'),
        (2, 'Seconde'),
        (3, 'Third'),
        (4, 'Fourth'),)

    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    year = models.IntegerField(choices=event_year, null=True, blank=True)
    image = models.ImageField(upload_to='', blank=True)
    
