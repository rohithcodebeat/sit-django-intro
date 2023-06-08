from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

    created_at = models.DateTimeField(auto_now_add=True)



class UserProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="user_user_profile")
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserPostsModels(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="user_posts_model")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # []
    likes = models.ManyToManyField(UserModel, related_name="user_post_likes", blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

