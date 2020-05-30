from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addComment, name='addComment')
    # ex: /home/2/
    # path('<int:question_id>/', views.detail, name="detail"),
]