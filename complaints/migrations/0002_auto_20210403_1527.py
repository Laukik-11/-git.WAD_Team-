# Generated by Django 3.1.3 on 2021-04-03 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'ordering': ['created']},
        ),
    ]
