# Generated by Django 5.1.1 on 2024-09-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[("TODO", "To Do"), ("INP", "In Process"), ("DONE", "Done")],
                default="TODO",
                max_length=10,
            ),
        ),
    ]
