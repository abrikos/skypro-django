from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name="catalog_list"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),

]