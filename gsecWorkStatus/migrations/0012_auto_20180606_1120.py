# Generated by Django 2.0.5 on 2018-06-06 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsecWorkStatus', '0011_auto_20180606_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='approved',
            new_name='approvedBy',
        ),
    ]