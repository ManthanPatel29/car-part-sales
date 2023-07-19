from django.urls import path
from .views import *
urlpatterns = [
    path('', home.as_view()),
    path('insert-part/', insert_part.as_view()),
    path('list-part/', list_part.as_view()),
    path('update-part/<int:pk>', update_list.as_view()),
    path('delete-part/<int:pk>', delete_list.as_view()),
]