from django.shortcuts import render, redirect
from .models import proyek as Proyek
from .models import dokumen as Dokumen
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test

def login_check(user):
    if user.is_authenticated:
        if user.is_superuser:
            return redirect('dashboard')
        else:
            return redirect('karyawan')
    return False
  
def is_superuser(user):
    return user.is_superuser
  
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        from django.contrib.auth import authenticate, login
        from django.contrib import messages
        
        user = authenticate(request, username=username, password=password)
        try:
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('dashboard')
                else:
                    return redirect('karyawan')
            else:
                raise Exception('Username atau password salah')
        except Exception as e:
            messages.error(request, str(e))
            
    return render(request, 'login.html')

@login_required
@user_passes_test(is_superuser)
def dashboard(request):
  return render(request, 'CustomAdmin/index.html')

@login_required
@user_passes_test(is_superuser)
def crudproyek(request):
    # Mengambil semua data proyek
    data_proyek = Proyek.objects.all()
    context = {'proyek': data_proyek}
    
    # Handle tambah proyek
    if request.GET.get('tambah'):
        if request.method == 'POST':
            proyek.objects.create(
                nama_proyek=request.POST.get('nama_proyek'),
                nama_paket_pekerjaan=request.POST.get('nama_paket_pekerjaan'),
                sub_bidang_pekerjaan=request.POST.get('sub_bidang_pekerjaan'),
                peruntukan_bangunan=request.POST.get('peruntukan_bangunan'),
                total_volume_atau_area=request.POST.get('total_volume_atau_area'),
                lokasi_proyek=request.POST.get('lokasi_proyek'),
                tanggal_mulai=request.POST.get('tanggal_mulai'),
                target_selesai=request.POST.get('target_selesai'),
                nama_client=request.POST.get('nama_client'),
                no_kontrak=request.POST.get('no_kontrak'),
                nilai_kontrak=request.POST.get('nilai_kontrak'),
                rencana_progress=request.POST.get('rencana_progress'),
                actual_progress=request.POST.get('actual_progress')
            )
            return redirect('crudproyek')
        context['tambah'] = True
        
    # Handle edit proyek
    elif request.GET.get('edit'):
        id_proyek = request.GET.get('edit')
        data = proyek.objects.get(id=id_proyek)
        if request.method == 'POST':
            data.nama_proyek = request.POST.get('nama_proyek')
            data.nama_paket_pekerjaan = request.POST.get('nama_paket_pekerjaan')
            data.sub_bidang_pekerjaan = request.POST.get('sub_bidang_pekerjaan')
            data.peruntukan_bangunan = request.POST.get('peruntukan_bangunan')
            data.total_volume_atau_area = request.POST.get('total_volume_atau_area')
            data.lokasi_proyek = request.POST.get('lokasi_proyek')
            data.tanggal_mulai = request.POST.get('tanggal_mulai')
            data.target_selesai = request.POST.get('target_selesai')
            data.nama_client = request.POST.get('nama_client')
            data.no_kontrak = request.POST.get('no_kontrak')
            data.nilai_kontrak = request.POST.get('nilai_kontrak')
            data.rencana_progress = request.POST.get('rencana_progress')
            data.actual_progress = request.POST.get('actual_progress')
            data.save()
            return redirect('crudproyek')
        context['edit'] = True
        context['proyek'] = data
        
    # Handle hapus proyek
    elif request.GET.get('hapus'):
        id_proyek = request.GET.get('hapus')
        proyek.objects.get(id=id_proyek).delete()
        return redirect('crudproyek')
        
    return render(request, 'CustomAdmin/crudproyek.html', context)

@login_required
@user_passes_test(is_superuser)
def cruddokumen(request):
    # Mengambil semua data dokumen
    data_dokumen = Dokumen.objects.all()
    context = {'dokumen': data_dokumen}
    
    # Handle tambah dokumen
    if request.GET.get('tambah'):
        if request.method == 'POST':
            Dokumen.objects.create(
                nama_dokumen=request.POST.get('nama_dokumen'),
                file=request.FILES.get('file')
            )
            return redirect('cruddokumen')
        context['tambah'] = True
        
    # Handle edit dokumen
    elif request.GET.get('edit'):
        id_dokumen = request.GET.get('edit')
        data = Dokumen.objects.get(id=id_dokumen)
        if request.method == 'POST':
            data.nama_dokumen = request.POST.get('nama_dokumen')
            if request.FILES.get('file'):
                data.file = request.FILES.get('file')
            data.save()
            return redirect('cruddokumen')
        context['edit'] = True
        context['dokumen'] = data
        
    # Handle hapus dokumen
    elif request.GET.get('hapus'):
        id_dokumen = request.GET.get('hapus')
        Dokumen.objects.get(id=id_dokumen).delete()
        return redirect('cruddokumen')
        
    return render(request, 'CustomAdmin/cruddokumen.html', context)

@login_required
@user_passes_test(is_superuser)
def print_proyek(request, id):
    data = Proyek.objects.get(id=id)
    context = {
        'proyek': data
    }
    return render(request, 'CustomAdmin/print_proyek.html', context)
  
def logout(request):
    auth_logout(request)
    return redirect('login')
  
  
@login_required
@user_passes_test(login_check)
def karyawan(request):
    return render(request, 'karyawan/karyawan.html')
  
@login_required
@user_passes_test(login_check)
def proyek(request):
    data_proyek = Proyek.objects.all()
    context = {'proyek': data_proyek}
    return render(request, 'karyawan/proyek.html', context)

@login_required
@user_passes_test(login_check)
def dokumen(request):
    data_dokumen = Dokumen.objects.all()
    context = {'dokumen': data_dokumen}
    return render(request, 'karyawan/dokumen.html', context)
