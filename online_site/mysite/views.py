from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets,generics,status,permissions
from .serializers import *
from .models import *
from .permissions import CreateClothes,CreateCategory
from .filters import ClothesFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class UserProfileAPIView(generics.ListAPIView):
    queryset =UserProfile.objects.all()
    serializer_class =UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)



class UserProfileDetailAPIViView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserProfileEditSerializers
        return UserProfileDetailSerializers



class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class  = CategoryDetailSerializers



class CategoryCreateAPIView(generics.ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class  = CategoryCreateSerializers
     permission_classes = [CreateCategory]



class CategoryEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class  = CategoryEDITSerializers
    permission_classes =[CreateCategory]



class ClothesListAPIView(generics.ListAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = ClothesFilter
    search_fields = ['clothes_name']
    ordering_fields = ['prise']



class ClothesCreateAPIView(generics.ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesCreateSerializers
    permission_classes = [CreateClothes]


class ClothesEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesEDITSerializer
    permission_classes = [CreateClothes]



class ClothesDetailAPIView(generics.RetrieveAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesDetailSerializers




class ClothesReviewListAPIView(generics.ListCreateAPIView):
    queryset = ClothesReview.objects.all()
    serializer_class = ClothesListReviewSerializers


class ClothesReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothesReview.objects.all()
    serializer_class = ClothesDetailReviewSerializers


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartIemListAPIView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class =CartItemSerializers
