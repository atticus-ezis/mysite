from django.urls import path
from .views import search, create_author, update_author, delete_author, contact, register_user, login_user, logout_view
from books import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    # search contact create
    path('', views.book_display, name = "book_display"),
    path('<int:pk>/', views.book_details, name = "book_details"),
    path("search/", search, name="search"),
    path('create_author/', create_author, name="create_author"),
    path('author/<int:pk>/', views.author_profile, name = "author_profile"),
    path("<int:pk>/update/", update_author, name="update_author"),
    path("<int:pk>/delete/", delete_author, name="delete_author"),
    path('contact/', contact, name="contact"),
    path('search_publisher/', views.SearchPublisher.as_view(), name="search_publisher"),
    path('search_author/', views.SearchAuthor.as_view(), name="search_author"),
    path('create_book/', views.CreateBookView.as_view(), name="create_book"),
    path('create_publisher/', views.CreatePublisher.as_view(), name="create_publisher"),
    
    path('update_book/<int:pk>/', views.UpdateBook.as_view(), name="update_book" ),
    path('update_publisher/<int:pk>/', views.UpdatePublisher.as_view(), name="update_publisher"),

    path('delete_book/<int:pk>/', views.DeleteBook.as_view(), name="delete_book" ),
   
    path('delete_publisher/<int:pk>/', views.DeletePublisher.as_view(), name="delete_publisher"),
    path('user/register/', register_user, name="register_user"),
    path('user/login/', login_user, name="login_user"),
    path('user/logout/', logout_view, name="logout"),

]
