from django.contrib import admin
from .models import dokumen, proyek
from django.db import models
from django.utils.html import format_html
from django.urls import path, reverse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

@admin.register(proyek)
class ProyekAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nama_proyek', 'nama_paket_pekerjaan', 'sub_bidang_pekerjaan', 'peruntukan_bangunan', 'total_volume_atau_area', 'lokasi_proyek',
        'section_separator_1',
        'tanggal_mulai', 'target_selesai',
        'section_separator_2',
        'nama_client',
        'section_separator_3',
        'no_kontrak', 'nilai_kontrak',
        'section_separator_4',
        'rencana_progress_persen', 'actual_progress_persen', 'tanggal_update',
        'section_separator_5',
        'get_print_button'
    )
    search_fields = ('nama_proyek', 'nama_paket_pekerjaan')
    fieldsets = (
        ('Informasi Proyek', {
            'fields': ('nama_proyek', 'nama_paket_pekerjaan', 'sub_bidang_pekerjaan', 'peruntukan_bangunan', 'total_volume_atau_area', 'lokasi_proyek')
        }),
        ('Tanggal', {
            'fields': ('tanggal_mulai', 'target_selesai')
        }),
        ('Informasi Client', {
            'fields': ('nama_client',)
        }),
        ('Kontrak', {
            'fields': ('no_kontrak', 'nilai_kontrak')
        }),
        ('Progress', {
            'fields': ('rencana_progress', 'actual_progress')
        }),
    )
    readonly_fields = ('tanggal_update',)
    actions = ['print_selected_proyek']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('print_all/', self.admin_site.admin_view(self.print_all_proyek), name='print_all_proyek'),
            path('<int:proyek_id>/print/', self.admin_site.admin_view(self.print_proyek), name='print_proyek'),
        ]
        return custom_urls + urls

    def get_print_button(self, obj):
        url = reverse('admin:print_proyek', args=[obj.id])
        return format_html('<a class="button" href="{}">Cetak</a>', url)
    get_print_button.short_description = 'Cetak'

    def section_separator_1(self, obj):
        return format_html('<hr style="border-top: 2px solid #000; margin: 10px 0;">')
    section_separator_1.short_description = ''

    def section_separator_2(self, obj):
        return format_html('<hr style="border-top: 2px solid #000; margin: 10px 0;">')
    section_separator_2.short_description = ''

    def section_separator_3(self, obj):
        return format_html('<hr style="border-top: 2px solid #000; margin: 10px 0;">')
    section_separator_3.short_description = ''

    def section_separator_4(self, obj):
        return format_html('<hr style="border-top: 2px solid #000; margin: 10px 0;">')
    section_separator_4.short_description = ''

    def section_separator_5(self, obj):
        return format_html('<hr style="border-top: 2px solid #000; margin: 10px 0;">')
    section_separator_5.short_description = ''

    def print_proyek(self, request, proyek_id):
        proyek_obj = proyek.objects.get(id=proyek_id)
        return self.generate_pdf([proyek_obj], is_detail=True)

    def print_all_proyek(self, request):
        proyek_list = proyek.objects.all()
        return self.generate_pdf(proyek_list)

    def print_selected_proyek(self, request, queryset):
        return self.generate_pdf(queryset)
    print_selected_proyek.short_description = "Cetak proyek yang dipilih"

    def generate_pdf(self, proyek_list, is_detail=False):
        if is_detail:
            template = get_template('admin/proyek_print_detail.html')
            filename = f'proyek_detail_{proyek_list[0].id}.pdf'
            context = {'proyek_list': proyek_list}
        else:
            template = get_template('admin/proyek_print_all.html')
            filename = 'proyek_list.pdf'
            # Menambahkan informasi kolom ke context
            context = {
                'proyek_list': proyek_list,
                'list_display': [field for field in self.list_display if field != 'get_print_button' and not field.startswith('section_separator_')],
                'header': [self.model._meta.get_field(field).verbose_name.title() if field != 'id' else 'No' for field in self.list_display if field != 'get_print_button' and not field.startswith('section_separator_')]
            }
        
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        
        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
        return HttpResponse('Error generating PDF', status=400)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['print_all_url'] = reverse('admin:print_all_proyek')
        return super().changelist_view(request, extra_context=extra_context)

    def get_list_display(self, request):
        return [self.center_text(field) if not field.startswith('section_separator_') and field != 'get_print_button' else field for field in self.list_display]

    def center_text(self, field_name):
        def inner(obj):
            value = getattr(obj, field_name)
            return format_html('<div style="text-align: center;">{}</div>', value)
        inner.short_description = field_name
        return inner

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_print_button'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_print_button'] = False
        return super().add_view(request, form_url, extra_context=extra_context)

    class Media:
        js = ('admin/js/print_button.js',)

@admin.register(dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ('nama_dokumen', 'tanggal_upload', 'tanggal_update')
    search_fields = ('nama_dokumen',)
    readonly_fields = ('tanggal_upload', 'tanggal_update')

    def get_list_display(self, request):
        return [self.center_text(field) for field in self.list_display]

    def center_text(self, field_name):
        def inner(obj):
            value = getattr(obj, field_name)
            return format_html('<div style="text-align: center;">{}</div>', value)
        inner.short_description = field_name
        return inner
