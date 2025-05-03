from PIL.DdsImagePlugin import item
from django.db import models
from django .contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True,blank=True,unique=True)
    ROLES_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
    )
    user_role = models.CharField(max_length=16, choices=ROLES_CHOICES, default='client')


    def __str__(self):
        return f'{self.last_name},{self.username}'


class Category(models.Model):
    category_name =models.CharField(max_length=40,unique=True)
    category_image = models.ImageField(upload_to='category_image/')

    def __str__(self):
        return f'{self.category_name}'


class Clothes(models.Model):
    clothes_name = models.CharField(max_length=40)
    clothes_image =models.ImageField(upload_to='clothes_image/')
    category = models.ForeignKey(Category,related_name='category_clothes',on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1,null=True,blank=True)
    description =models.TextField(null=True,blank=True)
    prise = models.DecimalField(max_digits=7,decimal_places=2)
    size = models.CharField(max_length=10, null=True, blank=True)
    brand = models.CharField(max_length=40, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.clothes_name}'

    def get_avg_rating(self):
        ratings = self.clothes_review.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 1 )
        return 0

    def get_count_rating(self):
        ratings = self.clothes_review.all()
        if ratings.exists():
            if ratings.count() > 500:
                return '500+'
            return ratings.count()
            return 0

    def get_good_grate(self):
        ratings = self.clothes_review.all()
        if ratings.exists():
            total_people = 0
            for i in ratings:
                if i.rating > 3:
                    total_people += 1
            return f'{(total_people * 100) / ratings.count()}%'

        return '0%'


class ClothesReview(models.Model):
    user =models.ForeignKey(UserProfile,related_name='user_review',on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes,on_delete=models.CASCADE, related_name='clothes_review')
    rating =models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user},{self.rating}'







class Cart(models.Model):
    client_cart = models.ForeignKey(UserProfile,related_name='client_cart',on_delete=models.CASCADE)



    def __str__(self):
       return f'{self.client_cart}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE,)
    clothes = models.ForeignKey(Clothes,related_name='clothes_cart',on_delete=models.CASCADE)
    quantity_cart =models.PositiveSmallIntegerField(default=1)


    # def get_total_prise(self):
    #     return self.clothes.prise * self.quantity_cart

    def __str__(self):
        return f'{self.clothes}'





