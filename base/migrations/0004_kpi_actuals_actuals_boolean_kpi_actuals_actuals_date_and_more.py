# Generated by Django 4.0.4 on 2023-04-03 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_smtp_configure'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi_actuals',
            name='actuals_boolean',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='kpi_actuals',
            name='actuals_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='kpi_actuals',
            name='actuals',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='kpi_actuals',
            name='perspective_id',
            field=models.ForeignKey(db_column='perspective_id', on_delete=django.db.models.deletion.CASCADE, to='base.perspectives'),
        ),
        migrations.CreateModel(
            name='initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scorecard_description', models.CharField(max_length=500)),
                ('action_item', models.CharField(max_length=500)),
                ('target_date', models.DateTimeField()),
                ('ownership', models.CharField(max_length=100)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_by', models.IntegerField()),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.CharField(default='N', max_length=1)),
                ('kpi_id', models.ForeignKey(db_column='kpi_id', on_delete=django.db.models.deletion.CASCADE, to='base.kpi_details')),
                ('objective_id', models.ForeignKey(db_column='objective_id', on_delete=django.db.models.deletion.CASCADE, to='base.business_goals_objectives')),
                ('perspective_id', models.ForeignKey(db_column='perspective_id', on_delete=django.db.models.deletion.CASCADE, to='base.scorecard_details')),
                ('scorecard_id', models.ForeignKey(db_column='scorecard_id', on_delete=django.db.models.deletion.CASCADE, to='base.scorecard')),
            ],
            options={
                'db_table': 'tb_sc_initiative3',
            },
        ),
    ]