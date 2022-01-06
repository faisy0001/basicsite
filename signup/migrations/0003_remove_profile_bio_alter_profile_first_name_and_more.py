# Generated by Django 4.0 on 2022-01-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_remove_profile_email_alter_profile_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
