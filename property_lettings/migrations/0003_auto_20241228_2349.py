# Generated by Django 3.0 on 2024-12-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property_lettings", "0002_alter_address_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="letting",
            name="id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
