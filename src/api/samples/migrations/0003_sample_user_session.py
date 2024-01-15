# Generated by Django 4.2.7 on 2024-01-04 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0001_initial'),
        ('samples', '0002_alter_sample_sample_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='user_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='user_sessions.usersession'),
        ),
    ]