# Generated by Django 4.0.4 on 2023-07-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_session_expired_session_lasttime_session_logintime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='lasttime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='logintime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]