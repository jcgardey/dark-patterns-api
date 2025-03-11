# Generated by Django 4.2.7 on 2025-03-10 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0004_remove_website_group_website_group'),
        ('user_sessions', '0006_alter_usersession_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='follow_up_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_ups', to='websites.websitegroup'),
        ),
    ]
