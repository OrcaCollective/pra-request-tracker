# Generated by Django 3.2.5 on 2021-07-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("record_requests", "0004_auto_20210718_0046"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agency",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="recordrequest",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="recordrequestfile",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]