# Generated by Django 3.2.13 on 2022-06-05 09:09

from django.db import migrations

import common.modelFields


class Migration(migrations.Migration):

    dependencies = [
        ("enrollments", "0009_alter_examthroughenrollment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="end_date",
            field=common.modelFields.ZeroSecondDateTimeField(verbose_name="end_date"),
        ),
        migrations.AlterField(
            model_name="session",
            name="start_date",
            field=common.modelFields.ZeroSecondDateTimeField(verbose_name="start_date"),
        ),
    ]
