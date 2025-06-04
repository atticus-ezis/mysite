from django.urls import path
from .views import search, create_author, update_author, delete_author, contact, search_publisher, search_author, create_book, update_book, delete_book, create_publisher, update_publisher, delete_publisher, register_user, login_user, logout_view

urlpatterns = [
    # search contact create
    path("search/", search, name="search"),
    path('create_author/', create_author, name="create_author"),
    path("<int:pk>/update/", update_author),
    path("<int:pk>/delete/", delete_author),
    path('contact/', contact, name="contact"),
    path('search_publisher/', search_publisher, name="search_publisher"),
    path('search_author/', search_author, name="search_author"),
    path('create_book/', create_book, name="create_book"),
    path('update_book/<int:pk>/', update_book, name="update_book" ),
    path('delete_book/<int:pk>/', delete_book, name="delete_book" ),
    path('create_publisher/', create_publisher, name="create_publisher"),
    path('update_publisher/<int:pk>/', update_publisher, name="update_publisher"),
    path('delete_publisher/<int:pk>/', delete_publisher, name="delete_publisher"),
    path('user/register/', register_user, name="register_user"),
    path('user/login/', login_user, name="login_user"),
    path('user/logout/', logout_view, name="logout"),
]
