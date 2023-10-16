# Generated by Django 4.0.4 on 2023-07-07 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_user_license_delete_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='pin_chart_to_homepage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chart_type', models.CharField(max_length=200)),
                ('order_no', models.IntegerField(default=0)),
                ('user_id', models.IntegerField()),
                ('pin_flag', models.CharField(default='Y', max_length=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_by', models.IntegerField()),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('kpi_id', models.ForeignKey(db_column='kpi_id', on_delete=django.db.models.deletion.CASCADE, to='base.kpi_details')),
            ],
            options={
                'db_table': 'tb_sc_pin_chart_to_homepage',
            },
        ),
    ]