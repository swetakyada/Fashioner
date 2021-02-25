from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addstudentinfo/$', views.addstudentinfo),
    path('delstudentinfo/', views.delstudentinfo,name='delstudentinfo'),
    url(r'^getstudentinfo/$', views.getstudentinfo),
    path('addsuccess/', views.addsuccess,name='addsuccess'),
    path('students/', views.StudentListView.as_view(), name = 'students'),
]