from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),  # Ubah dari '' menjadi 'dashboard/'
  path('crudproyek/', views.crudproyek, name='crudproyek'),
  path('cruddokumen/', views.cruddokumen, name='cruddokumen'),
  path('print_proyek/<int:id>', views.print_proyek, name='print_proyek'),
  path('logout/', views.logout, name='logout'),
  path('', views.login_view, name='login'),
  path('karyawan/', views.karyawan, name='karyawan'),
  path('proyek/', views.proyek, name='proyek'),
  path('dokumen/', views.dokumen, name='dokumen'),
]
