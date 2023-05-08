from django.urls import path
from adventures import views

urlpatterns = [
    path('adventures/', views.AdventureList.as_view()),
]