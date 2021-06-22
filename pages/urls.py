from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.SearchResultViews.as_view(), name='search_results'),
]