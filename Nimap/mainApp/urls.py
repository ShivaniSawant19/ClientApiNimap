from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/',DetailClient.as_view()),
    path('', ListClient.as_view()),
    path('create', CreateClient.as_view()),
    path('delete/<int:pk>',DeleteClient.as_view())
]
