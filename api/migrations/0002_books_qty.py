# Generated by Django 4.1.3 on 2022-12-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
