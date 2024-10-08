from django.contrib import admin
from .models import dokumen, proyek

@admin.register(proyek)
class ProyekAdmin(admin.ModelAdmin):
    list_display = ('nama_paket_pekerjaan', 'sub_bidang_pekerjaan', 'peruntukan_bangunan', 'total_volume_atau_area', 'lokasi', 'tanggal_mulai', 'tanggal_selesai', 'PJ_atau_PPK_nama', 'PJ_atau_PPK_alamat_telp', 'kontrak_no_tgl', 'kontrak_nilai', 'sp_kontrak', 'sp_prestasi_kerja', 'tanggal_update')
    search_fields = ('nama_paket_pekerjaan',)
    fieldsets = (
        ('Informasi Proyek', {
            'fields': ('nama_paket_pekerjaan', 'sub_bidang_pekerjaan', 'peruntukan_bangunan', 'total_volume_atau_area', 'lokasi', 'deskripsi')
        }),
        ('Pengguna Jasa atau Penjabat Pembuat Komitmen', {
            'fields': ('PJ_atau_PBK_nama', 'PJ_atau_PBK_alamat_telp')
        }),
        ('Kontrak (dalam Rupiah termasuk PPN & PPh)', {
            'fields': ('kontrak_no_tgl', 'kontrak_nilai')
        }),
        ('Tanggal', {
            'fields': ('tanggal_mulai', 'tanggal_selesai', 'tanggal_update')
        }),
        ('Status Progress', {
            'fields': ('sp_kontrak', 'sp_prestasi_kerja')
        }),
    )

@admin.register(dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ('nama_dokumen', 'tanggal_upload')
    search_fields = ('nama_dokumen',)
