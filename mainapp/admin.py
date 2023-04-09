from django.contrib import admin
from .models import PostModel, UserProfile
# Register your models here.

admin.site.register(PostModel)
admin.site.register(UserProfile)