# Generated by Django 4.2.7 on 2024-05-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_website_ux_analyzer_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='group',
        ),
        migrations.AddField(
            model_name='website',
            name='group',
            field=models.ManyToManyField(related_name='websites', to='websites.websitegroup'),
        ),
    ]