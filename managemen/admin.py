from django import forms
from django.contrib import admin
from django.db import models
from django.forms import ModelForm
from django.utils.html import format_html

from .models import dokumen, progress, proyek


# Register your models here.
@admin.register(proyek)
class ProyekAdmin(admin.ModelAdmin):
    list_display = ('nama_proyek', 'tanggal_mulai', 'tanggal_selesai', 'persentase_progress', 'status_terpilih')
    search_fields = ('nama_proyek',)
    list_filter = ('status',)

    def persentase_progress(self, obj):
        persentase = obj.persentase_terpilih
        return format_html(
            '<div style="width:120px; background-color: #f0f0f0; border: 1px solid #ddd; border-radius: 5px; overflow: hidden;">'
            '<div style="width: {}%; background-color: #4CAF50; height: 24px; transition: width 0.5s ease-in-out;"></div>'
            '<div style="text-align: center; margin-top: -24px; color: #333; font-weight: bold; text-shadow: 1px 1px 1px #fff;">{}</div>'
            '</div>',
            persentase, f"{persentase:.2f}%"
        )
    persentase_progress.short_description = 'Persentase'

    def status_terpilih(self, obj):
        status = obj.status_terpilih
        return status.replace('_', ' ').title()
    status_terpilih.short_description = 'Status'

@admin.register(dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ('nama_dokumen', 'tanggal_upload', 'persentase_progress', 'status_terpilih')
    search_fields = ('nama_dokumen',)
    list_filter = ('status',)

    def persentase_progress(self, obj):
        persentase = obj.persentase_terpilih
        return format_html(
            '<div style="width:120px; background-color: #f0f0f0; border: 1px solid #ddd; border-radius: 5px; overflow: hidden;">'
            '<div style="width: {}%; background-color: #4CAF50; height: 24px; transition: width 0.5s ease-in-out;"></div>'
            '<div style="text-align: center; margin-top: -24px; color: #333; font-weight: bold; text-shadow: 1px 1px 1px #fff;">{}</div>'
            '</div>',
            persentase, f"{persentase:.2f}%"
        )
    persentase_progress.short_description = 'Persentase'

    def status_terpilih(self, obj):
        status = obj.status_terpilih
        return status.replace('_', ' ').title()
    status_terpilih.short_description = 'Status'


@admin.register(progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('nama_progress', 'persentase', 'status', 'tanggal_update', 'tipe')
    search_fields = ('nama_progress',)
    list_filter = ('status', 'tipe')
