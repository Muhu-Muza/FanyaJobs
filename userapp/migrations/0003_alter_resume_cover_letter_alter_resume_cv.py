# Generated by Django 4.0.6 on 2022-10-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_resume_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='resume',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]