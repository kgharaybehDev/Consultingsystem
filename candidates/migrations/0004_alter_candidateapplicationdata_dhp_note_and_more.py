# Generated by Django 5.1.2 on 2024-11-13 01:20

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0003_alter_candidateapplicationdata_dhp_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidateapplicationdata",
            name="DHP_note",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Note"
            ),
        ),
        migrations.AlterField(
            model_name="candidateapplicationdata",
            name="TravelDetails_note",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Note"
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="job_responsibilities",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text="Enter the job responsibilities.",
                null=True,
                verbose_name="Job Responsibilities",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcandidateapplicationdata",
            name="DHP_note",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Note"
            ),
        ),
        migrations.AlterField(
            model_name="historicalcandidateapplicationdata",
            name="TravelDetails_note",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Note"
            ),
        ),
        migrations.AlterField(
            model_name="historicalexperience",
            name="job_responsibilities",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text="Enter the job responsibilities.",
                null=True,
                verbose_name="Job Responsibilities",
            ),
        ),
        migrations.AlterField(
            model_name="historicaltrainingcourse",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text="Provide additional details about the course, such as the subjects covered or skills acquired.",
                null=True,
                verbose_name="Description",
            ),
        ),
        migrations.AlterField(
            model_name="trainingcourse",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text="Provide additional details about the course, such as the subjects covered or skills acquired.",
                null=True,
                verbose_name="Description",
            ),
        ),
    ]
