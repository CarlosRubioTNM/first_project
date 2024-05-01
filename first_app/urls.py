from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns =[
    path('', views.index, name='index'),
    path('formpage/', views.form_name_view, name='form_name'),
]
