from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path("api/", views.ProductListView.as_view(), name="store_home"),
    path("api/<slug:slug>/", views.ProductItemView.as_view(), name="products"),
    path('api/category/', views.CategoryListView.as_view(), name='categories'),
    path('api/category/<slug:slug>',
         views.CategoryItemView.as_view(), name='category_item')
]
