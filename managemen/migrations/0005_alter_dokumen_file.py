# Generated by Django 5.0.7 on 2024-10-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managemen', '0004_dokumen_selected_progress_proyek_selected_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokumen',
            name='file',
            field=models.FileField(upload_to='dokumen/'),
        ),
    ]