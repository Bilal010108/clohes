from django.contrib import admin
from .models import *




admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Clothes)
admin.site.register(ClothesReview)
admin.site.register(Cart)
admin.site.register(CartItem)