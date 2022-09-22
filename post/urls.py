from django.urls import path
from .views import (
   profile,PostCreateView,PostListView,PostUpdateView,PostDeleteView,MyPostsView,ProfileEditView , UserListView
)
app_name = 'post'
urlpatterns = [
   path('create/', PostCreateView.as_view(), name='create'),
   path('postlist/',PostListView.as_view(),name='postlist'),
   path('update/<int:pk>',PostUpdateView.as_view(),name='update'),
   path('delete/<int:pk>',PostDeleteView.as_view(), name='delete'),
   path('mypost/',MyPostsView.as_view(), name='mypost'),
   path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'), 
   path('userlist/',  UserListView.as_view(), name='userlist'),
   path('profile/' ,profile, name='profile'),
]