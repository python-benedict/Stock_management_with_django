from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_view'),    #this url is for the home view
    path('Articles/create_article/', views.create_article, name="create_article"),
    path('Articles/', views.search_view, name='search_view'), #this usl is for searching
    path('Articles/<str:id>/', views.detailed_page, name="detailed_page")   #this url is for the page detailed view
]