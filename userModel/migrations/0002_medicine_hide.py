# Generated by Django 2.2.2 on 2019-07-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='hide',
            field=models.CharField(default='可见', max_length=100),
        ),
    ]
