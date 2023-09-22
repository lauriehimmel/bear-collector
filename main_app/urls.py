from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bears/', views.bears_index, name='bears_index'),
    path('bears/<int:bear_id>/', views.bears_detail, name='bears_detail'),
    path('bears/create/', views.BearCreate.as_view(), name='bears_create'),
    path('bears/<int:pk>/update/', views.BearUpdate.as_view(), name='bears_update'),
    path('bears/<int:pk>/delete/', views.BearDelete.as_view(), name='bears_delete'),
    path('bears/<int:bear_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('bears/<int:bear_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('food/', views.FoodList.as_view(), name='food_index'),
    path('food/<int:pk>/', views.FoodDetail.as_view(), name='food_detail'),
    path('food/create/', views.FoodCreate.as_view(), name='food_create'),
    # path('food/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
    # path('food/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
]