from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
# api viw url
path('article_lists',views.article_lists),
path('article_details/<int:pk>/',views.article_details),
path('update_article/<int:pk>/',views.update_article),
path('delete_article/<int:pk>/',views.delete_article),
#Regular view url
# path('article_list/',views.article_list),
# path('article_detail/<int:pk>/', views.article_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
