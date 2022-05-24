

from django.urls import path, include

from .views import delete, list, post


urlpatterns = [
    path('books/', list),
    path('books/create', post),
    path('books/delete/<int:pk>', delete),
    # path('journals/', )
]