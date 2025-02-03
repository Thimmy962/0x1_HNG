from django.urls import path, include
from . import view

urlpatterns = [
    path("api/classify-number", view.index)
]
