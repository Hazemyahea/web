# Generated by Django 2.2.3 on 2019-09-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0005_quest_cooldown_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]