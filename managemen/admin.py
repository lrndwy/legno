from django import forms
from django.contrib import admin
from django.db import models
from django.forms import ModelForm
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import dokumen, proyek


# Register your models here.
@admin.register(proyek)
class ProyekAdmin(admin.ModelAdmin):
    list_display = ('nama_paket_pekerjaan', 'sub_bidang_pekerjaan', 'peruntukan_bangunan', 'total_volume_atau_area', 'lokasi', 'tanggal_mulai', 'tanggal_selesai', 'tanggal_update', 'pengguna_jasa_atau_pbk', 'kontrak_info', 'status_progress')
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
            'fields': ('tanggal_mulai', 'tanggal_selesai')
        }),
        ('Status Progress', {
            'fields': ('sp_kontrak', 'sp_prestasi_kerja')
        }),
    )

    def pengguna_jasa_atau_pbk(self, obj):
        return format_html(
            '<table style="border-collapse: collapse; width: 100%;">'
            '<tr>'
            '<td style="padding: 8px; width: 50%;"><strong>Nama:</strong><br>{}</td>'
            '<td style="padding: 8px; width: 50%;"><strong>Alamat/Telp:</strong><br>{}</td>'
            '</tr>'
            '</table>',
            obj.PJ_atau_PBK_nama, obj.PJ_atau_PBK_alamat_telp
        )
    pengguna_jasa_atau_pbk.short_description = 'Pengguna Jasa / Pejabat Pembuat Komitmen'

    def kontrak_info(self, obj):
        return format_html(
            '<table style="border-collapse: collapse; width: 100%;">'
            '<tr>'
            '<td style="padding: 8px; width: 50%;"><strong>No/Tgl:</strong><br>{}</td>'
            '<td style="padding: 8px; width: 50%;"><strong>Nilai:</strong><br>Rp {}</td>'
            '</tr>'
            '</table>',
            obj.kontrak_no_tgl, '{:,}'.format(obj.kontrak_nilai).replace(',', '.')
        )
    kontrak_info.short_description = 'Kontrak'

    def status_progress(self, obj):
        return mark_safe(
            '<table style="border-collapse: collapse; width: 100%;">'
            '<tr>'
            '<td style="padding: 8px; width: 50%;"><strong>Kontrak:</strong><br>'
            '<div style="width:120px; background-color: #f0f0f0; border: 1px solid #ddd; border-radius: 5px; overflow: hidden;">'
            '<div style="width: {}%; background-color: #4CAF50; height: 24px; transition: width 0.5s ease-in-out;"></div>'
            '<div style="text-align: center; margin-top: -24px; color: #333; font-weight: bold; text-shadow: 1px 1px 1px #fff;">{:.2f}%</div>'
            '</div>'
            '</td>'
            '<td style="padding: 8px; width: 50%;"><strong>Prestasi Kerja:</strong><br>'
            '<div style="width:120px; background-color: #f0f0f0; border: 1px solid #ddd; border-radius: 5px; overflow: hidden;">'
            '<div style="width: {}%; background-color: #4CAF50; height: 24px; transition: width 0.5s ease-in-out;"></div>'
            '<div style="text-align: center; margin-top: -24px; color: #333; font-weight: bold; text-shadow: 1px 1px 1px #fff;">{:.2f}%</div>'
            '</div>'
            '</td>'
            '</tr>'
            '</table>'.format(obj.sp_kontrak, obj.sp_kontrak, obj.sp_prestasi_kerja, obj.sp_prestasi_kerja)
        )
    status_progress.short_description = 'Status Progress'

@admin.register(dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ('nama_dokumen', 'tanggal_upload')
    search_fields = ('nama_dokumen',)

