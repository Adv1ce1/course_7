# Generated by Django 4.2.5 on 2023-10-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("habit", "0005_habit_weekday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True,
                help_text="Вознаграждение за выполнение привычки.",
                max_length=255,
            ),
        ),
    ]
