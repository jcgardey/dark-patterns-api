# Generated by Django 4.2.7 on 2024-02-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_websitegroup_order'),
        ('samples', '0003_sample_user_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='websites.website'),
        ),
    ]
