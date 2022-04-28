from django.urls import  path
from news import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
path('news_list/',views.NewsList.as_view()),
path('news_list/<int:pk>/',views.NewsDetail.as_view()),
]
