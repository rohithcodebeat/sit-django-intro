from django.contrib import admin
from .models import UserModel, UserProfileModel, UserPostsModels
# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(UserPostsModels)
