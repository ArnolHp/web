from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('xa-hoi/', views.xa_hoi_page, name='xa_hoi'),
    path('chinh-tri/', views.chinh_tri_page, name='chinh_tri'),
    path('the-thao/', views.the_thao_page, name='the_thao'),
    path('suc-khoe/', views.suc_khoe_page, name='suc_khoe'),
    path('cong-nghe/', views.cong_nghe_page, name='cong_nghe'),
]
