# Generated by Django 4.2.7 on 2024-03-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0003_usersession_age_usersession_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
