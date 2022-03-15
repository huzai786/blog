from django.urls import path
from .views import (
    BlogDetail, 
    EditBlog, 
    DeleteBlog, 
    CreateBlog, 
    ListBlog, 
    MyBlog, 
    ViewProfile,
    EditProfile
    )



urlpatterns = [
    path('', ListBlog.as_view(), name='home'),
    path('my-blogs/', MyBlog.as_view(), name='my-blogs'),
    path('create-blog/', CreateBlog.as_view(), name='blog-create'),
    path('blog-detail/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('edit-blog/<int:pk>/', EditBlog.as_view(), name='blog-edit'),
    path('delete-blog/<int:pk>/', DeleteBlog.as_view(), name='blog-delete'),
    path('profile/<str:pk>/', ViewProfile.as_view(), name='profile'),
    path('edit-profile/<str:pk>/', EditProfile.as_view(), name='edit-profile'),
]   