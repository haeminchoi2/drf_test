from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name="ArticleList"),
]
