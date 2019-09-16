# Generated by Django 2.0.9 on 2018-12-24 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0029_auto_20181224_1042")]

    operations = [
        migrations.CreateModel(
            name="Gebruiksrechten",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "omschrijving_voorwaarden",
                    models.TextField(
                        help_text="Omschrijving van de van toepassing zijnde voorwaarden aan het gebruik anders dan raadpleging",
                        verbose_name="omschrijving voorwaarden",
                    ),
                ),
                (
                    "startdatum",
                    models.DateTimeField(
                        help_text="Begindatum van de periode waarin de gebruiksrechtvoorwaarden van toepassing zijn. Doorgaans is de datum van creatie van het informatieobject de startdatum.",
                        verbose_name="startdatum",
                    ),
                ),
                (
                    "einddatum",
                    models.DateTimeField(
                        blank=True,
                        help_text="Einddatum van de periode waarin de gebruiksrechtvoorwaarden van toepassing zijn.",
                        null=True,
                        verbose_name="startdatum",
                    ),
                ),
                (
                    "informatieobject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.EnkelvoudigInformatieObject",
                    ),
                ),
            ],
            options={
                "verbose_name": "gebruiksrecht informatieobject",
                "verbose_name_plural": "gebruiksrechten informatieobject",
            },
        )
    ]
