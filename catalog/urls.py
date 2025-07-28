from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name="catalog_list"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('category/<int:pk>/', views.ProductListViewByCategory.as_view(), name="product_category"),
    path('add/', views.CatalogCreateView.as_view(), name='catalog_add'),
    path('update/<int:pk>', views.CatalogUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', views.CatalogDeleteView.as_view(), name='product_delete'),

]