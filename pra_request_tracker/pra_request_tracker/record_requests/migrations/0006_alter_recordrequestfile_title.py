# Generated by Django 3.2.5 on 2021-07-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("record_requests", "0005_auto_20210718_1938"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recordrequestfile",
            name="title",
            field=models.CharField(blank=True, default=str, max_length=256),
            preserve_default=False,
        ),
    ]
