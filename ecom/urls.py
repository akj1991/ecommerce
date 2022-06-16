from django.urls import path
from .import views

urlpatterns = [
    path('', views.adminlogin,name="adminlogin"),
    path('forgotpass/', views.forgotpass,name="forgotpass"),
    path('dashboard/', views.adminhomefun,name="adminhome"),
    path('dashboard/register_mobile/', views.registmobile,name="registmobile"),
    path('dashboard/manage_product/', views.managepro,name="managepro"),
    path('registration1/',views.regifun1,name='registration1'),
    path('loaddata/',views.loaddata),
    path('deletedata/',views.deletebutton),
    path('updatedata/',views.updatebutton),
    path('updated/',views.updatefun),
]