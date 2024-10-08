from django.urls import path
from .admin import ProyekAdmin

urlpatterns = [
    path('managemen/proyek/<int:proyek_id>/print/', ProyekAdmin.print_proyek, name='print_proyek'),
    path('managemen/proyek/print_all/', ProyekAdmin.print_all_proyek, name='print_all_proyek'),
]
