# Generated by Django 4.2.5 on 2023-10-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("habit", "0006_alter_habit_reward"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="is_starting",
            field=models.BooleanField(default=False),
        ),
    ]
