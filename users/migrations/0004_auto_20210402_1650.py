# Generated by Django 3.1.3 on 2021-04-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210402_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='flatNo',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
