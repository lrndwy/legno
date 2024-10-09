from django.urls import path
from .admin import ProyekAdmin
from django.contrib import admin

urlpatterns = [
    path('proyek/<int:proyek_id>/print/', ProyekAdmin.print_proyek, name='print_proyek'),
    path('proyek/print_all/', ProyekAdmin.print_all_proyek, name='print_all_proyek'),
]
