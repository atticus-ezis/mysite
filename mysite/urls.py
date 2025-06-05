"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, current_datetime, hours_ahead, sum, date_check
from books.views import book_display, book_details, author_profile, display_classifications, classification_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('time/', current_datetime, name='current_time'),
    path('time/plus/<int:offset>/', hours_ahead, name = 'hours_ahead'),
    path('math/<int:number_1>/<int:number_2>/', sum, name = 'sum'),
    path('valid-date/<int:year>/<int:month>/<int:day>', date_check, name = "date_check"),
    path('classifications/', display_classifications, name="display_classifications"),
    path('classification-profile/<int:pk>/', classification_profile, name = "classification_profile"),  
    path('books/', include('books.urls')),
]
