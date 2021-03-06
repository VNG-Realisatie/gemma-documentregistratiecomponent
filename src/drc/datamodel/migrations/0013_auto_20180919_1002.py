# Generated by Django 2.0.6 on 2018-09-19 10:02

from django.db import migrations, models
from django.utils import timezone
import vng_api_common.validators


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0012_auto_20180815_1609")]

    operations = [
        migrations.RenameModel(
            old_name="ZaakInformatieObject", new_name="ObjectInformatieObject"
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="object",
            field=models.URLField(
                help_text="URL naar het gerelateerde OBJECT.", default=""
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="object_type",
            field=models.CharField(
                choices=[("besluit", "Besluit"), ("zaak", "Zaak")],
                max_length=100,
                verbose_name="objecttype",
                default="",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="titel",
            field=models.CharField(
                blank=True,
                help_text="De naam waaronder het INFORMATIEOBJECT binnen het OBJECT bekend is.",
                max_length=200,
                verbose_name="titel",
            ),
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="beschrijving",
            field=models.TextField(
                blank=True,
                help_text="Een op het object gerichte beschrijving van de inhoud vanhet INFORMATIEOBJECT.",
                max_length=1000,
                verbose_name="beschrijving",
            ),
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="registratiedatum",
            field=models.DateTimeField(
                help_text="De datum waarop de behandelende organisatie het INFORMATIEOBJECT heeft geregistreerd bij het OBJECT. Geldige waardes zijn datumtijden gelegen op of voor de huidige datum en tijd.",
                validators=[vng_api_common.validators.UntilNowValidator()],
                verbose_name="registratiedatum",
                default=timezone.now(),
            ),
            preserve_default=False,
        ),
    ]
