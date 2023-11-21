from django.urls import path
# Импортируем созданное нами представление
from .views import (
    NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete,
    ArticlesCreate, ArticlesUpdate, ArticlesDelete, ProtectedView, CategoryListView, CategoryName,
    subscribe, unsubscribe,
)


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   path('news/', NewsList.as_view(), name = 'news'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('news/<int:pk>/', NewsDetail.as_view(),name='news_detail'),
   path('news/search/', NewsSearch.as_view(), name = 'news_search'),

   path('news/create/', NewsCreate.as_view(),name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(),name='news_edit'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(),name='news_delete'),

   path('articles/create/', ArticlesCreate.as_view(),name='articles_create'),
   path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(),name='articles_edit'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(),name='articles_delete'),
   path('news/', ProtectedView.as_view(), name = 'news'),

   path('categories/<int:pk>/', CategoryListView.as_view(),name='category_list'),
   path('categories/', CategoryName.as_view(),name='category_name'),
   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),

]
