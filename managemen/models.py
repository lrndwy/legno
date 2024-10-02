from django.db import models


# Create your models here.
class proyek(models.Model):
    nama_proyek = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    tanggal_update = models.DateField(auto_now=True)
    STATUS_CHOICES = [
        ('belum', 'Belum'),
        ('sedang_berjalan', 'Sedang Berjalan'),
        ('selesai', 'Selesai'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='belum')
    selected_progress = models.ForeignKey('progress', on_delete=models.SET_NULL, null=True, blank=True, related_name='selected_for_proyek')
    
    def __str__(self):
        return self.nama_proyek
    
    def get_latest_progress(self):
        return self.progress_set.order_by('-tanggal_update').first()
    
    @property
    def persentase_terbaru(self):
        latest_progress = self.get_latest_progress()
        return latest_progress.persentase if latest_progress else 0

    @property
    def persentase_terpilih(self):
        selected_progress = self.get_selected_progress()
        return selected_progress.persentase if selected_progress else 0
    
    @property
    def status_terpilih(self):
        selected_progress = self.get_selected_progress()
        return selected_progress.status if selected_progress else 'belum'

    def get_selected_progress(self):
        return self.selected_progress or self.progress_set.filter(tipe='proyek').order_by('-tanggal_update').first()

    class Meta:
        verbose_name = "proyek"
        verbose_name_plural = "proyek"


class dokumen(models.Model):
    nama_dokumen = models.CharField(max_length=255)
    file = models.FileField(upload_to='dokumen/')
    tanggal_upload = models.DateField(auto_now_add=True)
    tanggal_update = models.DateField(auto_now=True)
    STATUS_CHOICES = [
        ('belum', 'Belum'),
        ('sedang_berjalan', 'Sedang Berjalan'),
        ('selesai', 'Selesai'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='belum')
    selected_progress = models.ForeignKey('progress', on_delete=models.SET_NULL, null=True, blank=True, related_name='selected_for_dokumen')
    
    def __str__(self):
        return self.nama_dokumen
    
    def get_latest_status(self):
        return self.progress_set.order_by('-tanggal_update').filter(tipe='dokumen').first()
    
    @property
    def status_terbaru(self):
        latest_status = self.get_latest_status()
        return latest_status.status if latest_status else 'belum'
    
    def get_latest_progress(self):
        return self.progress_set.order_by('-tanggal_update').first()
    
    @property
    def persentase_terbaru(self):
        latest_progress = self.get_latest_progress()
        return latest_progress.persentase if latest_progress else 0

    @property
    def persentase_terpilih(self):
        selected_progress = self.get_selected_progress()
        return selected_progress.persentase if selected_progress else 0
    
    @property
    def status_terpilih(self):
        selected_progress = self.get_selected_progress()
        return selected_progress.status if selected_progress else 'belum'

    def get_selected_progress(self):
        return self.selected_progress or self.progress_set.filter(tipe='dokumen').order_by('-tanggal_update').first()

    class Meta:
        verbose_name = "dokumen"
        verbose_name_plural = "dokumen"


class progress(models.Model):
    nama_progress = models.CharField(max_length=255)
    deskripsi = models.TextField()
    persentase = models.DecimalField(max_digits=5, decimal_places=2)
    tanggal_update = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('belum', 'Belum'),
        ('sedang_berjalan', 'Sedang Berjalan'),
        ('selesai', 'Selesai'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='belum')
    TIPE_CHOICES = [
        ('proyek', 'Proyek'),
        ('dokumen', 'Dokumen'),
    ]
    tipe = models.CharField(max_length=20, choices=TIPE_CHOICES, default='proyek')
    proyek = models.ForeignKey(proyek, on_delete=models.CASCADE, null=True, blank=True, related_name='progress_set')
    dokumen = models.ForeignKey(dokumen, on_delete=models.CASCADE, null=True, blank=True, related_name='progress_set')
    
    def __str__(self):
        return self.nama_progress
    
    def get_latest_status(self):
        return self.progress_set.order_by('-tanggal_update').filter(tipe='progress').first()
    
    @property
    def status_terbaru(self):
        latest_status = self.get_latest_status()
        return latest_status.status if latest_status else 'belum'

    class Meta:
        verbose_name = "progress"
        verbose_name_plural = "progress"
