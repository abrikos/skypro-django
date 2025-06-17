from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.BlogListView.as_view(), name='blog_posts'),
    path('add/', views.BlogCreateView.as_view(), name='blog_add'),
    path('update/<int:pk>', views.BlogUpdateView.as_view(), name='blog_update'),
    path('view/<int:pk>', views.BlogDetailView.as_view(), name='blog_view'),
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='blog_delete'),
]