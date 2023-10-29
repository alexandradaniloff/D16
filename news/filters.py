from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    date_create = DateFilter(field_name='date_create', widget=forms.DateInput(attrs={'type': 'date'}),
                             lookup_expr='date__gte')
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {
           # поиск по названию
           'author': ['iexact'],
           'title': ['icontains'],
           #'categories': ['iexact']


        }