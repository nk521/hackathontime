# Generated by Django 2.2.7 on 2019-12-05 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_users', '0006_auto_20191205_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(blank=True, to='hackathontime_users.Profile'),
        ),
    ]