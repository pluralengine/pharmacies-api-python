from django.urls import include, path

from . import views

app_name = 'pharmacies'
urlpatterns = [
    path('', views.pharmacies_list),
    path('<int:pk>', views.pharmacy_detail),
]
