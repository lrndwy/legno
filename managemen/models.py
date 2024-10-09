from django.db import models

# Create your models here.
class proyek(models.Model):
    nama_proyek = models.CharField(max_length=255, verbose_name="Nama Proyek")
    nama_paket_pekerjaan = models.CharField(max_length=255, verbose_name="Nama Paket Pekerjaan")
    sub_bidang_pekerjaan = models.CharField(max_length=255, verbose_name="Sub Bidang Pekerjaan")
    peruntukan_bangunan = models.CharField(max_length=255, verbose_name="Peruntukan Bangunan")
    total_volume_atau_area = models.CharField(max_length=255, verbose_name="Total Volume atau Area")
    lokasi_proyek = models.CharField(max_length=255, verbose_name="Lokasi Proyek")
    tanggal_mulai = models.DateField(verbose_name="Tanggal Mulai")
    target_selesai = models.DateField(verbose_name="Target Selesai")
    nama_client = models.CharField(max_length=255, verbose_name="Nama Client")
    no_kontrak = models.CharField(max_length=255, verbose_name="Nomor Kontrak")
    nilai_kontrak = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Nilai Kontrak")
    rencana_progress = models.IntegerField(verbose_name="Rencana Progress (%)")
    actual_progress = models.IntegerField(verbose_name="Actual Progress (%)")
    tanggal_update = models.DateField(auto_now=True, verbose_name="Tanggal Update")
    
    @property
    def rencana_progress_persen(self):
        return f"{self.rencana_progress}%"
    
    @property
    def actual_progress_persen(self):
        return f"{self.actual_progress}%"
    
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
