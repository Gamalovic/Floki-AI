# Generated by Django 2.0.4 on 2018-07-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0003_auto_20180519_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.TextField(default='write something about yourself ...', max_length=500),
        ),
    ]
