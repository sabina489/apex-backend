# Generated by Django 3.2.13 on 2022-06-13 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_course_options"),
        ("enrollments", "0013_merge_20220613_1556"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursethroughenrollment",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_enrolls",
                to="courses.course",
            ),
        ),
        migrations.AlterField(
            model_name="coursethroughenrollment",
            name="enrollment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_enrolls",
                to="enrollments.enrollment",
            ),
        ),
        migrations.AlterField(
            model_name="coursethroughenrollment",
            name="selected_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_enrolls",
                to="enrollments.session",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="courses",
            field=models.ManyToManyField(
                related_name="enrolls",
                through="enrollments.CourseThroughEnrollment",
                to="courses.Course",
            ),
        ),
        migrations.AlterField(
            model_name="examthroughenrollment",
            name="selected_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exam_enrolls",
                to="enrollments.session",
                verbose_name="exam_session",
            ),
        ),
    ]