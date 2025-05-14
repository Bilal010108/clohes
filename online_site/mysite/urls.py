from .views import *
from rest_framework import routers
from django.urls import  path,include


router = routers.SimpleRouter()




urlpatterns = [
    path('', include(router.urls)),

    path('user_profile/',UserProfileAPIView.as_view(),name = 'user_profile'),
    path('user_profile/<int:pk>/',UserProfileDetailAPIViView.as_view(),name = 'user_detail'),

    path('category/',CategoryListAPIView.as_view(),name = 'category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category_create/',CategoryCreateAPIView.as_view(),name='category_create_list'),
    path('category_create/<int:pk>/',CategoryEditAPIView.as_view(),name = 'category_edit'),


    path('clothes/',ClothesListAPIView.as_view(),name = 'clothes_list'),
    path('clothes/<int:pk>/',ClothesDetailAPIView.as_view(),name='clothes_detail'),
    path('clothes_create/', ClothesCreateAPIView.as_view(), name='clothes_create_list'),
    path('clothes_create/<int:pk>/', ClothesEditAPIView.as_view(), name='clothes_create_detail'),

    path('clothes_review/', ClothesReviewListAPIView.as_view(), name='clothes_review_list'),
    path('clothes_review/<int:pk>/', ClothesReviewDetailAPIView.as_view(), name='clothes_review_detail'),

    path('cart/', CartListAPIView.as_view(), name='clothes_review_list'),
    path('cartitem/<int:pk>/', CartIemListAPIView.as_view(), name='clothes_review_detail'),
]

