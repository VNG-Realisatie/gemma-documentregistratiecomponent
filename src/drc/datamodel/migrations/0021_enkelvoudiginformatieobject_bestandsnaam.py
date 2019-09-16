# Generated by Django 2.0.6 on 2018-12-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0020_objectinformatieobject_aard_relatie")]

    operations = [
        migrations.AddField(
            model_name="enkelvoudiginformatieobject",
            name="bestandsnaam",
            field=models.CharField(
                blank=True,
                help_text="De naam van het fysieke bestand waarin de inhoud van het informatieobject is vastgelegd, inclusief extensie.",
                max_length=255,
                verbose_name="bestandsnaam",
            ),
        )
    ]
