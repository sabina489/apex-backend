# Generated by Django 3.2.13 on 2022-12-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0009_auto_20221201_1705"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacherattendancedetail",
            name="number_of_period",
            field=models.DecimalField(
                decimal_places=2, max_digits=4, verbose_name="Number_of_peroid"
            ),
        ),
    ]
