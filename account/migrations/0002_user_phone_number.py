# Generated by Django 5.0.2 on 2024-04-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=20, verbose_name="phone number"
            ),
        ),
    ]