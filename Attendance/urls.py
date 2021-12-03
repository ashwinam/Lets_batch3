from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home" ),
  path("name", views.name, name="name"),
  path("dis", views.DataDsiplay, name="display"),
  path("distable", views.DataDsiplayStudent, name="displaytable"),
  path("disform", views.student_form_data, name="displayform"),
  path("disformmodel", views.student_form_data_model, name="displayformmodel"),
  path("masterdetails", views.master_Data, name="masterdetails"),
  path("mark_att", views.Mark_Att, name="markatt"),
  path("dis_att", views.display_attendance, name="disatt"),
  path("oneatt", views.Mark_Att, name="OneAtt"),


]
