# Generated by Django 5.1.2 on 2024-11-03 02:20

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "code",
                    models.CharField(
                        db_index=True,
                        max_length=3,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Country Code",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Country Name")),
            ],
            options={
                "verbose_name": "Country",
                "verbose_name_plural": "Countries",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="DegreeChoices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("Bachelor", "Bachelor"),
                            ("Master", "Master"),
                            ("PhD", "PhD"),
                            ("Diploma", "Diploma"),
                        ],
                        help_text="Enter the degree obtained (e.g., Bachelor, Master).",
                        max_length=255,
                        unique=True,
                        verbose_name="Degree",
                    ),
                ),
            ],
            options={
                "verbose_name": "Degree",
                "verbose_name_plural": "Degrees",
                "ordering": ["degree"],
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        blank=True,
                        help_text="Enter a unique abbreviation for the department, e.g., HR, IT.",
                        max_length=10,
                        null=True,
                        verbose_name="Abbreviation",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Enter the official title of the department, if different from the name.",
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="Title",
                    ),
                ),
            ],
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="EducationGradeChoices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        help_text="Enter the grade obtained (e.g., Excellent, Good).",
                        max_length=255,
                        unique=True,
                        verbose_name="Grade",
                    ),
                ),
            ],
            options={
                "verbose_name": "Grade",
                "verbose_name_plural": "Grades",
                "ordering": ["grade"],
            },
        ),
        migrations.CreateModel(
            name="FieldOfStudy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "field_of_study",
                    models.CharField(
                        help_text="Enter the field of study.",
                        max_length=255,
                        verbose_name="Field of Study",
                    ),
                ),
            ],
            options={
                "verbose_name": "Field of Study",
                "verbose_name_plural": "Fields of Study",
                "ordering": ["field_of_study"],
            },
        ),
        migrations.CreateModel(
            name="LanguageChoices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        help_text="Enter the language.",
                        max_length=255,
                        unique=True,
                        verbose_name="Language-Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
                "ordering": ["language"],
            },
        ),
        migrations.CreateModel(
            name="Nationality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nationality_name",
                    models.CharField(max_length=100, verbose_name="Nationality Name"),
                ),
            ],
            options={
                "verbose_name": "Nationality",
                "verbose_name_plural": "Nationalities",
                "ordering": ["nationality_name"],
            },
        ),
        migrations.CreateModel(
            name="HistoricalCountry",
            fields=[
                (
                    "code",
                    models.CharField(
                        db_index=True, max_length=3, verbose_name="Country Code"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Country Name")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Country",
                "verbose_name_plural": "historical Countries",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDegreeChoices",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("Bachelor", "Bachelor"),
                            ("Master", "Master"),
                            ("PhD", "PhD"),
                            ("Diploma", "Diploma"),
                        ],
                        db_index=True,
                        help_text="Enter the degree obtained (e.g., Bachelor, Master).",
                        max_length=255,
                        verbose_name="Degree",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Degree",
                "verbose_name_plural": "historical Degrees",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDepartment",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        blank=True,
                        help_text="Enter a unique abbreviation for the department, e.g., HR, IT.",
                        max_length=10,
                        null=True,
                        verbose_name="Abbreviation",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        help_text="Enter the official title of the department, if different from the name.",
                        max_length=255,
                        null=True,
                        verbose_name="Title",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Department",
                "verbose_name_plural": "historical Departments",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalEducationGradeChoices",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        db_index=True,
                        help_text="Enter the grade obtained (e.g., Excellent, Good).",
                        max_length=255,
                        verbose_name="Grade",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Grade",
                "verbose_name_plural": "historical Grades",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalFieldOfStudy",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "field_of_study",
                    models.CharField(
                        help_text="Enter the field of study.",
                        max_length=255,
                        verbose_name="Field of Study",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Field of Study",
                "verbose_name_plural": "historical Fields of Study",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalInstitution",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "institution",
                    models.CharField(
                        help_text="Enter the institution.",
                        max_length=255,
                        verbose_name="Institution",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("University", "University"), ("college", "college")],
                        help_text="Enter the type of institution.",
                        max_length=255,
                        verbose_name="Institution Type",
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text="Enter the abbreviation of the institution.",
                        max_length=255,
                        null=True,
                        verbose_name="Institution Abbreviation",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        help_text="Select the country of the educational institution.",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="utilities.country",
                        verbose_name="Country",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Institution",
                "verbose_name_plural": "historical Institutions",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalLanguageChoices",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        db_index=True,
                        help_text="Enter the language.",
                        max_length=255,
                        verbose_name="Language-Name",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Language",
                "verbose_name_plural": "historical Languages",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalNationality",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "nationality_name",
                    models.CharField(max_length=100, verbose_name="Nationality Name"),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Nationality",
                "verbose_name_plural": "historical Nationalities",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "institution",
                    models.CharField(
                        help_text="Enter the institution.",
                        max_length=255,
                        verbose_name="Institution",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("University", "University"), ("college", "college")],
                        help_text="Enter the type of institution.",
                        max_length=255,
                        verbose_name="Institution Type",
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text="Enter the abbreviation of the institution.",
                        max_length=255,
                        null=True,
                        verbose_name="Institution Abbreviation",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        help_text="Select the country of the educational institution.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="utilities.country",
                        verbose_name="Country",
                    ),
                ),
            ],
            options={
                "verbose_name": "Institution",
                "verbose_name_plural": "Institutions",
                "ordering": ["type", "institution"],
            },
        ),
    ]
