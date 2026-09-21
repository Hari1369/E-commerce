from django.contrib import admin
from django.urls import path
from .views import main_dashboard, brand_registration, product_registration, subproduct, brand_update




urlpatterns = [
    path('', main_dashboard, name="main_page"),
    path('brand_page/', brand_registration, name="brand_registration"),
    path("brand_update/<int:brand_id>/", brand_update, name="brand_update"),


    path('product_page/', product_registration, name="product_page"),
    path('subproduct_page/', subproduct, name="subproduct_page")

]
