from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('products/', views.products, name='products'),
    path('products/new', views.products_new, name='products_new'),
    path('products/edit/<int:id>', views.products_edit, name='products_edit'),
    path('productgallery/<int:id>', views.products_gallery, name='products_gallery'),
]