# Generated by Django 3.1.3 on 2021-04-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210414_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
