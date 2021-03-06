# Generated by Django 3.2.7 on 2021-09-19 13:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('plate', models.CharField(default='00 ABC 99', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('latitude', models.FloatField(default=32.32)),
                ('longitude', models.FloatField(default=33.33)),
                ('vehicle', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='navigationrecord.vehicle')),
            ],
        ),
    ]
