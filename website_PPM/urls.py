from django.urls import path
from .views import HomePageView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, CreateCategoryView, \
    CategoryView, CategoryListView, LikeView, CreateCommentView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('create_post/', CreatePostView.as_view(), name="create_post"),
    path('create_category/', CreateCategoryView.as_view(), name="create_category"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>/', LikeView.as_view(), name='like_post'),
    path('post/<int:pk>/comment/', CreateCommentView.as_view(), name="create_comment"),

]