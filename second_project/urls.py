from django.contrib import admin
from django.urls import path
# from second_app.views import book_list
from second_app.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list),
]
