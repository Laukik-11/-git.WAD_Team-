# Generated by Django 3.1.3 on 2021-04-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210402_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
