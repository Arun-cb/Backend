# Generated by Django 4.0.4 on 2023-07-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0021_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='permission',
            field=models.ForeignKey(db_column='permission', on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
