# Generated by Django 3.1.3 on 2020-11-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('rnum', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('co_survey', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'survey',
                'managed': False,
            },
        ),
    ]
