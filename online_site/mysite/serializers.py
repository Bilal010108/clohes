from.models import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model =UserProfile
        fields = ['id','user_role','username',]


class UserProfileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','phone_number','user_role','last_name','first_name','username']


class UserProfileEditSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','phone_number','last_name','first_name','username']


class ClothesListSerializers(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()
    good_grate = serializers.SerializerMethodField()

    class Meta:
        model = Clothes
        fields = ['id','clothes_name','clothes_image','prise','avg_rating','count_rating','good_grate']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()

    def get_good_grate(self, obj):
        return obj.get_good_grate()

class ClothesDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id','clothes_name','clothes_image','category',
                  'quantity','description','prise','size','brand',
                  'color','material','created_at','updated_at']


class ClothesCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'

class ClothesEDITSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'

class ClothesReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesReview
        fields = ['user','clothes','rating','comment']



class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['id','category_name','category_image']






class CategoryDetailSerializers(serializers.ModelSerializer):
    category_clothes=ClothesListSerializers(read_only=True, many=True)

    class Meta:
        model = Category
        fields= ['id','category_name','category_image','category_clothes']



class CategoryCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryEDITSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['client_cart']



class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields = ['cart','clothes','quantity_cart']


class ClothesListReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =ClothesReview
        fields = ['user','clothes','rating','comment']

class ClothesDetailReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =ClothesReview
        fields = ['user','clothes','rating','comment']