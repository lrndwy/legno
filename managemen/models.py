from django.db import models


# Create your models here.
class proyek(models.Model):
    nama_paket_pekerjaan = models.CharField(max_length=255, verbose_name="Nama Paket Pekerjaan")
    sub_bidang_pekerjaan = models.CharField(max_length=255, verbose_name="Sub Bidang Pekerjaan")
    peruntukan_bangunan = models.CharField(max_length=255, verbose_name="Peruntukan Bangunan")
    total_volume_atau_area = models.CharField(max_length=255, verbose_name="Total Volume atau Area")
    lokasi = models.CharField(max_length=255, verbose_name="Lokasi")
    PJ_atau_PPK_nama = models.CharField(max_length=255, verbose_name="Nama PJ atau PBK")
    PJ_atau_PPK_alamat_telp = models.CharField(max_length=255, verbose_name="Alamat dan Telepon PJ atau PBK")
    kontrak_no_tgl = models.CharField(max_length=255, verbose_name="Nomor dan Tanggal Kontrak")
    kontrak_nilai = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Nilai Kontrak")
    deskripsi = models.TextField(verbose_name="Deskripsi")
    tanggal_mulai = models.DateField(verbose_name="Tanggal Mulai")
    tanggal_selesai = models.DateField(verbose_name="Tanggal Selesai")
    tanggal_update = models.DateField(auto_now=True, verbose_name="Tanggal Update")
    sp_kontrak = models.IntegerField(verbose_name="Status Progress Kontrak (%)")
    sp_prestasi_kerja = models.IntegerField(verbose_name="Status Progress Prestasi Kerja (%)")


    def __str__(self):
        return self.nama_paket_pekerjaan

    class Meta:
        verbose_name = "proyek"
        verbose_name_plural = "proyek"


class dokumen(models.Model):
    nama_dokumen = models.CharField(max_length=255)
    file = models.FileField(upload_to="dokumen/")
    tanggal_upload = models.DateField(auto_now_add=True)
    tanggal_update = models.DateField(auto_now=True)
    def __str__(self):
        return self.nama_dokumen

    class Meta:
        verbose_name = "dokumen"
        verbose_name_plural = "dokumen"
