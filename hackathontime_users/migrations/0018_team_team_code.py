# Generated by Django 2.2.7 on 2019-12-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_users', '0017_team_team_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
