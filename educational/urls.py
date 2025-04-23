from django.urls import path
from . import views



app_name = "educational"
urlpatterns = [
    path('', views.DetailView.as_view())   
]
