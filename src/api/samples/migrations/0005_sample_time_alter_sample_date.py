# Generated by Django 4.2.7 on 2024-03-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_alter_sample_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='time',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
