# Generated by Django 4.2.3 on 2023-08-14 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_alter_usercategory_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercategory',
            unique_together=set(),
        ),
    ]
