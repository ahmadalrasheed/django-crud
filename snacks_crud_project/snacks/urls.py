from django.urls import path
from .views import (
    SnackListView,
    SnackDetailView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView
)


urlpatterns = [
    path('' , SnackListView.as_view() , name='home'),
    path('<int:pk>/' , SnackDetailView.as_view() , name='snackdetails' ),
    path('create/' , SnackCreateView.as_view() , name='createsnack'),
    path('<int:pk>/update/' , SnackUpdateView.as_view()  , name='updatesnack'),
    path('<pk>/delete/', SnackDeleteView.as_view()),
]