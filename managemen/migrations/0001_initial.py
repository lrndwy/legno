# Generated by Django 5.1.1 on 2024-10-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dokumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dokumen', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='dokumen/')),
                ('tanggal_upload', models.DateField(auto_now_add=True)),
                ('tanggal_update', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('belum', 'Belum'), ('sedang_berjalan', 'Sedang Berjalan'), ('selesai', 'Selesai')], default='belum', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_progress', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('persentase', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tanggal_update', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('belum', 'Belum'), ('sedang_berjalan', 'Sedang Berjalan'), ('selesai', 'Selesai')], default='belum', max_length=20)),
                ('tipe', models.CharField(choices=[('proyek', 'Proyek'), ('dokumen', 'Dokumen')], default='proyek', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='proyek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_proyek', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('tanggal_update', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('belum', 'Belum'), ('sedang_berjalan', 'Sedang Berjalan'), ('selesai', 'Selesai')], default='belum', max_length=20)),
            ],
        ),
    ]
