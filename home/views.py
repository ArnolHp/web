from django.shortcuts import render

def homepage(request):
    return render(request, 'home_template/home.html')

def xa_hoi_page(request):
    return render(request, 'home_template/xa_hoi.html')

def chinh_tri_page(request):
    return render(request, 'home_template/chinh_tri.html')

def the_thao_page(request):
    return render(request, 'home_template/the_thao.html')

def suc_khoe_page(request):
    return render(request, 'home_template/suc_khoe.html')

def cong_nghe_page(request):
    return render(request, 'home_template/cong_nghe.html')
