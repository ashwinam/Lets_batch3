from django.urls import path, include
from .views import CreatePost, Allpost,SpecificPost
from . import views
# staring from post they are using class based view

urlpatterns = [
    path('createpost/', CreatePost, name='createpost'),
    #path('allpost/', Allpost, name='AllPost'),
    path('allpost/<int:id1>/', SpecificPost, name='sp_post'),

    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-sp'),
    path('pages/<int:page>/', Allpost, name='pages'),
    path('post/view/', views.PostListView.as_view(), name='post-all'),
    path('post/myposts/', views.UserPostListView.as_view(), name='user-post-all'),
    path('post/<str:u1>/', views.OtherUserPostListView.as_view(), name='other-post-all'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:id1>/', views.CommentPost, name='post-comment'),
    path('posts/<int:id1>/approve/', views.comment_approve, name='post-approve'),



    
   
]