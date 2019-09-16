# Generated by Django 2.0.6 on 2018-07-24 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0004_auto_20180701_0818")]

    operations = [
        migrations.AddField(
            model_name="enkelvoudiginformatieobject",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                help_text="Unieke resource identifier (UUID4)",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="zaakinformatieobject",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                help_text="Unieke resource identifier (UUID4)",
                null=True,
            ),
        ),
    ]
