# Generated by Django 5.1.2 on 2024-11-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "candidates",
            "0002_rename_medicaltest_fit_to_work_candidateapplicationdata_medicaltest_is_fit_to_work_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidateapplicationdata",
            name="DHP_Password",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="DHP Password"
            ),
        ),
        migrations.AlterField(
            model_name="historicalcandidateapplicationdata",
            name="DHP_Password",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="DHP Password"
            ),
        ),
    ]
