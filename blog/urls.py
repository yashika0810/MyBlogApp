from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/random',views.random, name='random'),
    # path('blog/edit/<int:id>', views.edit),
    path('blog/edit/<int:id>', views.update, name='update_detail'),
    path('blog/delete/<int:id>', views.delete, name='delete_detail'),


]



