# Generated by Django 4.2.7 on 2024-05-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0004_usersession_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
