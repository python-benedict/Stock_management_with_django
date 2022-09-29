from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('Articles/<str:id>/', views.detailed_page, name="detailed_page")
]